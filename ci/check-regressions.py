#!/usr/bin/env python
"""Check for regressions of building simple docs."""

import itertools
import json
import re
import sys
from pathlib import Path


def _get_expected_path():
    """Return the regression fixture for the supported Sphinx versions."""
    return Path("tests/data/regression.html")


def check_empty_search_index_json():
    """Ibid."""
    path = Path("doc/build/html/_static/search/search_index.json")
    if not path.exists():
        print(f"{path} does not exist")
        return False
    with path.open(encoding="utf8") as fd:
        try:
            json.load(fd)
        except json.JSONDecodeError:
            print(f"Could not decode json for {path}")
            raise
    return True


def diff_contents():
    """Check the contents to see if they match.

    Note: We have to do this manually so we can ignore certain changes, like
    cache-busting suffixes, generated copyright years, and other dynamic values.
    """
    cache_busting = re.compile(r"\?v=[0-9A-Fa-f]*")
    copyright_year = re.compile(r"2005-\d{4}")

    def normalize(line):
        line = cache_busting.sub("", line)
        return copyright_year.sub("2005-YYYY", line)

    expected = _get_expected_path()
    new = Path("doc/build/html/regression.html")

    with expected.open(encoding="utf8") as fd:
        expected_lines = fd.readlines()

    with new.open(encoding="utf8") as fd:
        new_lines = fd.readlines()

    for i, (expected_line, new_line) in enumerate(
        itertools.zip_longest(expected_lines, new_lines)
    ):
        expected_line, new_line = expected_line.strip(), new_line.strip()
        if normalize(expected_line) == normalize(new_line):
            continue

        print(f"on line {i}, `{expected_line}` != `{new_line}`")
        return False

    return True


if __name__ == "__main__":
    ret = True
    for fn in (
        check_empty_search_index_json,
        diff_contents,
    ):
        ret = fn() and ret
    if not ret:
        sys.exit(-1)
