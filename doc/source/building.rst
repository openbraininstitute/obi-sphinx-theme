Building the theme
==================

In order to build the theme, you must first checkout the
``obi-sphinx-theme`` source::

   git clone --recursive https://github.com/openbraininstitute/obi-sphinx-theme.git

This will also clone the ``mkdocs-material`` submodule which is required.
The submodule is pinned to Material for MkDocs 9.7.7 at commit
``b3e6dd886a974aa8200759ecfd7db28c598a2894``; the converter is not intended to
consume an arbitrary upstream checkout.

Building and testing the theme is very simple::

   tox

The tox environments first run ``translate_templates.py`` and then install the
resulting theme. To regenerate only the theme, run this command from the
repository root::

   python translate_templates.py

The converter copies the generated templates from
:file:`mkdocs-material/material/templates`, removes MkDocs-only integration
files and configured upstream blocks, prepends the Material license notices,
and overlays the local Sphinx templates from :file:`src`. It then renames the
copied :file:`assets` directory to :file:`static` for Sphinx.

Once the theme has been built, the theme will be located in the
:file:`obi_sphinx_theme` directory.

.. warning::

   You should never edit files in the :file:`obi_sphinx_theme` directory
   by hand, any changes will be overwritten next time someone builds the theme.
