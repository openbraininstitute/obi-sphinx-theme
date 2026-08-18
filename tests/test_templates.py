"""Regression checks for local Material template overrides."""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parents[1]


def test_local_html_overrides_parse_as_jinja():
    """Every local HTML override remains syntactically valid Jinja."""
    environment = Environment(
        loader=FileSystemLoader(ROOT / "src"),
        extensions=["jinja2.ext.i18n"],
    )

    for template_path in (ROOT / "src").rglob("*.html"):
        environment.parse(template_path.read_text(encoding="utf-8"))


def test_local_overrides_follow_material_977_contracts():
    """Local branding overrides retain the current Material template API."""
    header = (ROOT / "src/partials/header.html").read_text(encoding="utf-8")
    footer = (ROOT / "src/partials/footer.html").read_text(encoding="utf-8")
    social = (ROOT / "src/partials/social.html").read_text(encoding="utf-8")

    assert 'class = "md-header"' in header
    assert 'include "partials/palette.html"' in header
    assert 'include "partials/tabs.html"' in header
    assert '"material/search" in config.plugins' in header
    assert '"search" in config.plugins' in header
    assert 'include ".icons/" ~ icon ~ ".svg"' in header

    assert 'class="md-footer__inner md-grid"' in footer
    assert 'class="md-footer-nav"' not in footer
    assert '"navigation.footer" in features' in footer
    assert "config.theme.icon.previous" in footer
    assert "config.theme.icon.next" in footer

    assert "social.name | d(social.type, true)" in social
    assert 'class="md-social__link"' in social
    assert 'include ".icons/" ~ social.icon ~ ".svg"' in social
