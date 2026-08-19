Sample Page
===========

This page demonstrates the OBI theme's styling of standard Sphinx elements.

Headings
--------

Second-level heading
~~~~~~~~~~~~~~~~~~~~

Third-level heading
^^^^^^^^^^^^^^^^^^^

Text Formatting
---------------

This is a paragraph with **bold text**, *italic text*, and ``inline code``.

Here is a `link to pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io/>`_.

Lists
-----

- Item one
- Item two
- Item three with **emphasis**

1. First ordered item
2. Second ordered item
3. Third ordered item

Code Blocks
-----------

Python:

.. code-block:: python

   import numpy as np

   def hello(name: str) -> str:
       """Greet someone."""
       return f"Hello, {name}!"

   result = hello("OBI")
   print(result)

Bash:

.. code-block:: bash

   pip install obi-sphinx-theme

Admonitions
-----------

.. note::

   This is a note admonition.

.. warning::

   This is a warning admonition.

.. tip::

   This is a tip admonition.

.. danger::

   This is a danger admonition.

.. seealso::

   `pydata-sphinx-theme docs <https://pydata-sphinx-theme.readthedocs.io/>`_
   for more styling examples.

Tables
------

.. list-table:: OBI Color Palette
   :header-rows: 1

   * - Role
     - Color
   * - Brand / Buttons
     - Navy ``#002766``
   * - Selections
     - Light blue ``#d6ebff`` / ``#bae0ff``
   * - Panels
     - Soft blue-grey ``#f5f8fa`` / ``#edf2f7``
   * - Background
     - White ``#ffffff``
   * - Text
     - Dark ``#141414`` / ``#262626``

Blockquote
----------

    "The brain is wider than the sky."
    — Emily Dickinson

Math
----

Inline math: :math:`E = mc^2`

Display math:

.. math::

   \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
