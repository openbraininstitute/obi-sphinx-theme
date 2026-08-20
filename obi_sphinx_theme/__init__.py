"""Open Brain Institute Sphinx Theme.

A thin wrapper around pydata-sphinx-theme with OBI brand colors.
"""

from pathlib import Path

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0+unknown"

_THEME_PATH = Path(__file__).parent


def setup(app):
    """Register the theme with Sphinx."""
    app.add_html_theme("obi_sphinx_theme", str(_THEME_PATH))
    app.connect("builder-inited", _set_obi_defaults)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def _set_obi_defaults(app):
    """Set OBI logo and favicon defaults if not overridden by the user."""
    logo = str(_THEME_PATH / "static" / "images" / "obi-logo-white.svg")
    favicon = str(_THEME_PATH / "static" / "images" / "obi-favicon.ico")

    # Set logo if user hasn't specified one
    if not app.config.html_logo:
        app.config.html_logo = logo

    # Set favicon if user hasn't specified one
    if not app.config.html_favicon:
        app.config.html_favicon = favicon
