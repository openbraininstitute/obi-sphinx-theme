"""Override autodoc output to wrap in a div."""

from docutils import nodes
import sphinx.ext.autodoc as sea
from sphinx.ext.autodoc.directive import AutodocDirective as LegacyAutodocDirective

try:
    # The modern directive was introduced in Sphinx 9. Keep this import
    # optional so the theme remains compatible with older Sphinx versions.
    from sphinx.ext.autodoc._directive import (
        AutodocDirective as ModernAutodocDirective,
    )
except ImportError:  # pragma: no cover - exercised only with Sphinx < 9
    ModernAutodocDirective = None


def _wrap_autodoc_output(result):
    """Wrap generated autodoc nodes in the theme's container."""
    container = nodes.container()
    container["classes"].append("autodoc-output")
    container += result
    return [container]


class AutodocDirectiveOverride(LegacyAutodocDirective):
    """Extend the legacy autodoc directive to wrap output in a div."""

    def run(self):
        """Wrap the autodoc output in a div with autodoc class."""
        return _wrap_autodoc_output(super().run())


if ModernAutodocDirective is not None:

    class ModernAutodocDirectiveOverride(ModernAutodocDirective):
        """Extend the modern Sphinx 9 autodoc directive."""

        def run(self):
            """Wrap the autodoc output in a div with autodoc class."""
            return _wrap_autodoc_output(super().run())

else:  # pragma: no cover - exercised only with Sphinx < 9
    ModernAutodocDirectiveOverride = AutodocDirectiveOverride


_MODERN_AUTODOC_TYPES = (
    "module",
    "class",
    "exception",
    "function",
    "decorator",
    "method",
    "property",
    "attribute",
    "data",
    "type",
)


def _add_legacy_autodoc_overrides(app):
    """Override legacy autodoc directives based on registered Documenters."""
    # These are found by looking for class members named `objtype` in
    # sphinx/ext/autodoc/__init__.py
    documenters = [
        "ModuleDocumenter",
        "FunctionDocumenter",
        "DecoratorDocumenter",
        "ClassDocumenter",
        "ExceptionDocumenter",
        "DataDocumenter",
        "MethodDocumenter",
        "AttributeDocumenter",
        "PropertyDocumenter",
        # removed in https://github.com/sphinx-doc/sphinx/pull/10700/files
        # and released in v6.1.2
        "NewTypeDataDocumenter",
        "NewTypeAttributeDocumenter",
    ]
    allowed_missing = {
        "NewTypeDataDocumenter",
        "NewTypeAttributeDocumenter",
    }

    for documentor_name in documenters:
        try:
            documentor = getattr(sea, documentor_name)
        except AttributeError as e:
            if documentor_name in allowed_missing:
                continue
            raise e

        app.add_directive(
            "auto" + documentor.objtype, AutodocDirectiveOverride, override=True
        )


def _add_modern_autodoc_overrides(app):
    """Override the directive types provided by Sphinx's modern autodoc."""
    for objtype in _MODERN_AUTODOC_TYPES:
        app.add_directive(
            "auto" + objtype,
            ModernAutodocDirectiveOverride,
            override=True,
        )


def add_autodoc_override(app):
    """Override autodoc directives to wrap their output in a div."""
    if "sphinx.ext.autodoc" not in app.extensions:
        return

    # Sphinx 9 defaults to the modern implementation. Sphinx < 9 has no
    # autodoc_use_legacy_class_based setting and always uses the legacy path.
    if getattr(app.config, "autodoc_use_legacy_class_based", True):
        _add_legacy_autodoc_overrides(app)
    else:
        _add_modern_autodoc_overrides(app)
