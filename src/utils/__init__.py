"""Module of utilities for translation between mkdocs and Sphinx."""

from obi_sphinx_theme.utils.toc_builder import build_tocs
from obi_sphinx_theme.utils.inject_context import inject_context_variables
from obi_sphinx_theme.utils.filters import add_filters
from obi_sphinx_theme.utils.autodoc_override import add_autodoc_override
from obi_sphinx_theme.utils.metadata import write_metadata, write_metadata_sphinx
from obi_sphinx_theme.utils.search_builder import copy_search_index_json
