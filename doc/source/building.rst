Building the theme
==================

In order to build the theme, you must first checkout the
``obi-sphinx-theme`` source::

   git clone --recursive https://github.com/openbraininstitute/obi-sphinx-theme.git

This will also clone the ``mkdocs-material`` submodule which is required.

Building and testing the theme is very simple::

   tox

This will run the necessary conversion scripts and copy the required source
files.

Once the theme has been built, the theme will be located in the
:file:`obi_sphinx_theme` directory.

.. warning::

   You should never edit files in the :file:`obi_sphinx_theme` directory
   by hand, any changes will be overwritten next time someone builds the theme.
