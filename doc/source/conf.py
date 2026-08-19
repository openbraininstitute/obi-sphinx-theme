"""Configuration file for the Sphinx documentation builder."""

import importlib.metadata

# -- Project information -----------------------------------------------------

project = "obi-sphinx-theme"
version = importlib.metadata.version("obi-sphinx-theme")
release = version
author = "Open Brain Institute"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = "obi_sphinx_theme"
html_title = "OBI Sphinx Theme"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/openbraininstitute/obi-sphinx-theme",
            "icon": "fa-brands fa-github",
        },
    ],
    "navbar_align": "left",
}
