"""
Test for search index builder which is required for lunr
search used by mkdocs-material.
"""

import json

import pytest  # pylint: disable=unused-import
from obi_sphinx_theme.utils import search_builder


def test_index_entry():
    """
    Test the construction of the list of blocks from text.
    """
    text_list = ("Line one \u00b6.", "Line two.   ")
    entry = search_builder.IndexEntry()
    entry.text_list.extend(text_list)

    text = """Line one . Line two."""

    assert text == entry.text


def test_index_as_dict():
    """
    Test the returned dictionary representation.
    """
    text_list = ("Line one \u00b6.", "Line two.   ")
    entry = search_builder.IndexEntry(location="/", title="test")
    entry.text_list.extend(text_list)

    as_dict = {"location": "/", "title": "test", "text": """Line one . Line two."""}

    assert as_dict == entry.as_dict()


def test_search_index_config():
    """Test the Material search configuration in the generated index."""
    index = search_builder.SearchIndexBuilder()
    data = json.loads(repr(index))

    assert data["config"] == {
        "fields": {
            "tags": {"boost": 1e6},
            "text": {"boost": 1e0},
            "title": {"boost": 1e3},
        },
        "lang": ["en"],
        "pipeline": ["stopWordFilter"],
        "separator": r"[\s\-]+",
    }


def test_index_entry_normalizes_missing_title():
    """Search documents must use a string title for the Material search worker."""
    entry = search_builder.IndexEntry(title=None)

    assert entry.as_dict()["title"] == ""
