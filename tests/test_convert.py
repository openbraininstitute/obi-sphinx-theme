"""
Test for the conversion of files.
"""

from collections import defaultdict
from pathlib import Path

import pytest  # pylint: disable=unused-import
from mkdocs2sphinx.convert_files import convert_files, do_replacements, prepend_license
from translate_templates import _ignore_on_copy


def test_do_replacements():
    """
    Test replacements with text blocks.
    """
    stats = defaultdict(int)

    text = """This is some text
<a>specific_text</a>
Some text embedded in a <hello> line"""

    rep = {"specific_text": "first", "<hello>": "goodbye"}

    text = do_replacements(text, rep, stats)

    result = """This is some text
<a>first</a>
Some text embedded in a goodbye line"""

    assert text == result


def test_prepend_license():
    """
    Test the prepending of the license to text.
    """

    lic = "LICENSE"
    text = """This is some test
text that will be used to check licenses."""

    # first test an unknown file type
    lictext = prepend_license((lic,), text, ".py")
    assert lictext == text

    # test css
    lictext = prepend_license((lic,), text, ".css")
    assert lictext.startswith("/*\n * LICENSE")


def test_modern_template_copy_exclusions():
    """Exclude MkDocs-only files without excluding similarly named paths."""
    assert _ignore_on_copy(Path("material/templates"), []) == [
        "mkdocs_theme.yml",
        "main.html",
        "404.html",
    ]
    assert _ignore_on_copy(Path("material/templates/partials"), []) == ["integrations"]
    assert not _ignore_on_copy(Path("material/templates/assets/images"), [])
    assert not _ignore_on_copy(Path("material/templates/fragments/images"), [])


def test_prepend_license_html_and_javascript():
    """Material's license can be safely prepended to HTML and JavaScript."""
    lic = ("LICENSE",)
    text = "content"

    html = prepend_license(lic, text, ".HTML")
    javascript = prepend_license(lic, text, ".Js")

    assert html.startswith("{#\n<!--\n  LICENSE\n-->")
    assert javascript.startswith("/*\n * LICENSE\n */")


def test_javascript_source_maps_are_excluded():
    """Generated JavaScript source maps are not copied into the theme."""
    javascript_path = Path("material/templates/assets/javascripts")
    nested_javascript_path = javascript_path / "workers"
    stylesheet_path = Path("material/templates/assets/stylesheets")

    assert _ignore_on_copy(javascript_path, ["bundle.js.map", "bundle.js"]) == [
        "bundle.js.map"
    ]
    assert _ignore_on_copy(nested_javascript_path, ["search.js.map"]) == [
        "search.js.map"
    ]
    assert not _ignore_on_copy(stylesheet_path, ["main.css.map"])


def test_javascript_source_map_comments_are_removed(tmp_path):
    """Converted JavaScript does not refer to source maps that are not shipped."""
    script = tmp_path / "theme.js"
    script.write_text("content\n//# sourceMappingURL=theme.js.map\n", encoding="utf-8")

    convert_files(tmp_path, (), {}, ("LICENSE",), set())

    assert "sourceMappingURL" not in script.read_text(encoding="utf-8")
