"""This module will translate the mkdocs material theme to a Sphinx theme."""

import shutil
from pathlib import Path

from mkdocs2sphinx import copy_source, convert_files


def _ignore_on_copy(directory, contents):  # pylint: disable=unused-argument
    """Provides list of items to be ignored.

    Args:
        directory (Path): The path to the current directory.
        contents (list): A list of files in the current directory.

    Returns:
        list: A list of files to be ignored.
    """
    directory = Path(directory)
    if directory.name == "templates" and directory.parent.name == "material":
        return ["mkdocs_theme.yml", "main.html", "404.html"]

    if directory.name == "partials" and directory.parent.name == "templates":
        return ["integrations"]

    return []


if __name__ == "__main__":
    # set some paths
    PWD_PATH = Path(__file__).parent

    # this assumes that the mkdocs material theme is in the same directory
    # as this file's parent directory
    SRC_PATH = PWD_PATH / "mkdocs-material" / "material" / "templates"
    OUT_PATH = PWD_PATH / "obi_sphinx_theme"
    copy_source(SRC_PATH, OUT_PATH, _ignore_on_copy)

    # convert files from mkdocs to Sphinx
    BLOCK_LIST = ("source", "disqus", "analytics")
    # Material 9.7.7 uses root-relative `.icons/` template includes. Its
    # `assets/` references are URLs and must remain unchanged for the local
    # Sphinx URL filter to map them to `_static/`.
    REPLACEMENT_MAP = {}

    # ensure mkdocs-material licenses are included
    LICENSE_PATH = PWD_PATH / "mkdocs-material" / "LICENSE"
    LICENSE_TEXT = LICENSE_PATH.read_text(encoding="utf8").splitlines()
    shutil.copyfile(LICENSE_PATH, OUT_PATH / "MATERIAL-LICENSE.txt")
    FILES_NOT_NEEDING_LICENSE = {
        "font-awesome.css",  # license information already included
        "material-icons.css",  # license information already included
    }

    STATS = convert_files(
        OUT_PATH, BLOCK_LIST, REPLACEMENT_MAP, LICENSE_TEXT, FILES_NOT_NEEDING_LICENSE
    )

    # show all replacement rules
    print("Replacement rules running, see below for details:")
    print("[replaced string]: [number of occurrences]")
    for k, v in STATS.items():
        colour = "\033[31m" if v == 0 else "\033[32m"
        end_colour = "\033[0m"
        print(f"{colour}{k}: {v}{end_colour}")

    shutil.copytree(PWD_PATH / "src", OUT_PATH, dirs_exist_ok=True)

    # sphinx expects a 'static' directory so rename the mkdocs-material one
    (OUT_PATH / "assets").rename(OUT_PATH / "static")
