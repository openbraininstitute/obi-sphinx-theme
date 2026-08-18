"""Tests for the autodoc output wrapper."""

from pathlib import Path
import subprocess
import sys

import pytest
import sphinx


@pytest.mark.parametrize("legacy", [False, True])
def test_autodoc_override_supports_both_modes(tmp_path: Path, legacy: bool):
    """Wrap autodoc output when either Sphinx autodoc implementation is active."""
    source_dir = tmp_path / "source"
    output_dir = tmp_path / "output"
    doctree_dir = tmp_path / "doctrees"
    source_dir.mkdir()

    (source_dir / "sample_module.py").write_text(
        "def documented_function():\n"
        + '    """A function documented by autodoc."""\n',
        encoding="utf-8",
    )
    (source_dir / "conf.py").write_text(
        "import sys\n"
        f"sys.path.insert(0, {str(source_dir)!r})\n"
        "extensions = ['sphinx.ext.autodoc', 'obi_sphinx_theme']\n"
        "html_theme = 'obi-sphinx-theme'\n"
        "project = 'autodoc override test'\n"
        + (
            f"autodoc_use_legacy_class_based = {legacy!r}\n"
            if sphinx.version_info >= (9, 0)
            else ""
        ),
        encoding="utf-8",
    )
    (source_dir / "index.rst").write_text(
        "Autodoc override test\n"
        "=====================\n\n"
        ".. autofunction:: sample_module.documented_function\n",
        encoding="utf-8",
    )

    subprocess.run(
        [
            sys.executable,
            "-m",
            "sphinx",
            "-b",
            "html",
            "-W",
            "-q",
            "-d",
            str(doctree_dir),
            str(source_dir),
            str(output_dir),
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    html = (output_dir / "index.html").read_text(encoding="utf-8")
    assert 'class="autodoc-output docutils container"' in html
    assert "A function documented by autodoc." in html
