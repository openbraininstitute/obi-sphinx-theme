OBI Sphinx Theme
================

|build_status| |license| |black|

Introduction
------------

OBI Sphinx Theme is the Open Brain Institute documentation theme, based on the
Sphinx BlueBrain Theme.

You can view the |changelog| to see what has changed recently.

Installation
------------

You can install the theme using `pip`::

   pip install obi-sphinx-theme

Usage
-----

Refer to the |usage| for how to use the theme.

License
-------

The code for the theme is licensed under the MIT License.

The name "Blue Brain Project" is property of its respective owner and does not
fall under the MIT license.

The theme incorporates third party components which are listed below, along with their relevant licenses:

`Material for MkDocs 9.7.7 theme <https://squidfunk.github.io/mkdocs-material/>`__
   MIT License, see `the license <https://github.com/squidfunk/mkdocs-material/blob/9.7.7/LICENSE>`__.
`Open Sans font <https://fonts.google.com/specimen/Open+Sans>`__
   Apache License Version 2.0, see `the license <https://github.com/BlueBrain/sphinx-bluebrain-theme/blob/master/src/assets/fonts/open-sans/LICENSE.txt>`__.
`Titillium Web font <https://fonts.google.com/specimen/Titillium+Web>`__
   Open Font License Version 1.1, see `the license <https://github.com/BlueBrain/sphinx-bluebrain-theme/blob/master/src/assets/fonts/titillium-web/OFL.txt>`__.
OBI logo
   The OBI logo is copyright Open Brain Institute. All rights reserved.

About
-----

OBI Sphinx Theme is a Sphinx theme based on the Sphinx BlueBrain Theme and the
excellent *Material for MkDocs* theme by Martin Donath (@squidfunk).

The upstream Sphinx BlueBrain Theme is licensed under the MIT license and is
hosted on `GitHub <https://github.com/BlueBrain/sphinx-bluebrain-theme>`__.
You can see examples (and the associated ``rst`` source) in the |sample| page.

OBI Sphinx Theme is built through a combination of text replacement rules,
HTML template overrides, a small amount of additional CSS and Javascript, and
a Python module which injects additional required context.

Acknowledgement
---------------

The development of this software was supported by funding to the Blue Brain Project, a research center of the École polytechnique fédérale de Lausanne (EPFL), from the Swiss government’s ETH Board of the Swiss Federal Institutes of Technology.

Copyright (c) 2020-2024 Blue Brain Project/EPFL

Copyright (c) 2025-2026 Open Brain Institute


.. |build_status| image:: https://github.com/openbraininstitute/obi-sphinx-theme/actions/workflows/run-tox.yml/badge.svg
                     :target: https://github.com/openbraininstitute/obi-sphinx-theme/actions/workflows/run-tox.yml
                     :alt: Build Status

.. |license| image:: https://img.shields.io/pypi/l/obi-sphinx-theme
                :target: https://github.com/openbraininstitute/obi-sphinx-theme/blob/main/LICENSE.txt

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
              :target: https://github.com/psf/black

.. substitutions
.. |changelog| replace:: `changelog <CHANGELOG.rst>`__
.. |usage| replace:: `usage guide <doc/source/usage.rst>`__
.. |sample| replace:: `samples <doc/source/sample.rst>`__
