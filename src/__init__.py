"""obi_sphinx_theme package."""

from os import path

from obi_sphinx_theme import utils


def setup(app):
    """Initialise the theme and connect theme specific functions to events."""
    app.add_html_theme("obi-sphinx-theme", path.dirname(path.abspath(__file__)))
    app.setup_extension("obi_sphinx_theme.ext.tabs")
    app.setup_extension("obi_sphinx_theme.ext.details")
    app.setup_extension("obi_sphinx_theme.ext.iframe")
    app.connect("builder-inited", utils.add_filters)
    app.connect("builder-inited", utils.add_autodoc_override)
    app.connect("env-updated", utils.write_metadata_sphinx)
    app.connect("html-page-context", utils.build_tocs)
    app.connect("html-page-context", utils.inject_context_variables)
    app.connect("build-finished", utils.copy_search_index_json)
