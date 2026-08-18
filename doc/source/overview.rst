Methodology overview
====================

An overview of the methodology applied to create the OBI Sphinx Theme is
given below. The upstream Material source is the ``mkdocs-material`` submodule
pinned to Material for MkDocs 9.7.7.

#. User clones ``obi-sphinx-theme`` git repository::

      git clone --recursive https://github.com/openbraininstitute/obi-sphinx-theme.git

#. User runs the ``tox`` environment, or invokes the converter directly::

      tox
      python translate_templates.py

#. ``translate_templates.py`` copies the generated theme templates from
   :file:`mkdocs-material/material/templates` into
   :file:`obi_sphinx_theme`. MkDocs-only files at the template root and the
   integrations directory are excluded.
#. It applies conversion rules to files with ``.html``, ``.css``, ``.js``, and
   ``_t`` extensions:

   #. Clears the configured Jinja ``source``, ``disqus``, and ``analytics``
      blocks while preserving their block tags.
   #. Applies the configured string replacements. Material 9.7.7's
      root-relative ``.icons/`` includes and URL-style ``assets/`` references
      are retained for the Sphinx URL filter.
   #. Prepends the Material license to converted files when appropriate and
      writes the upstream license to :file:`MATERIAL-LICENSE.txt`.

#. It overlays the local Sphinx templates and support files from :file:`src`.
#. It renames the copied :file:`assets` directory to :file:`static`, as required
   by Sphinx.
