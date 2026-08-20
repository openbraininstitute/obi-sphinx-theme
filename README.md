# OBI Sphinx Theme

A Sphinx theme for [Open Brain Institute](https://openbraininstitute.org) projects.

[![Documentation Status](https://readthedocs.org/projects/obi-sphinx-theme/badge/?version=latest)](https://obi-sphinx-theme.readthedocs.io/en/latest/?badge=latest)

This is a thin wrapper around [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io/) that applies the OBI color palette:

| Role | Color |
|------|-------|
| Brand / Buttons | Navy `#002766` |
| Selections | Light blue `#d6ebff` / `#bae0ff` |
| Panels | Soft blue-grey `#f5f8fa` / `#edf2f7` |
| Editor / Background | White `#ffffff` |
| Text | Dark `#141414` / `#262626` |
| Scrollbars | Navy `#002766` |

## Installation

```bash
pip install obi-sphinx-theme
```

## Usage

In your project's `conf.py`:

```python
html_theme = "obi_sphinx_theme"
```

All [pydata-sphinx-theme options](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html) are supported via `html_theme_options`.

## Development

```bash
# Install in development mode
pip install -e .

# Build the demo docs
cd doc
make html
```

## License

Copyright (c) 2025 Open Brain Institute

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

See [LICENSE.txt](LICENSE.txt) for the complete notice.
