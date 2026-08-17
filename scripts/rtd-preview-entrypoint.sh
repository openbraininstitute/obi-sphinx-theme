#!/usr/bin/env bash
set -euo pipefail

rm -rf /workspace
mkdir -p /workspace
cp -a /src/. /workspace/
cd /workspace

python translate_templates.py

export READTHEDOCS="${READTHEDOCS:-True}"
if [[ -z "${SETUPTOOLS_SCM_PRETEND_VERSION+x}" ]] && ! git rev-parse --git-dir >/dev/null 2>&1; then
  export SETUPTOOLS_SCM_PRETEND_VERSION=0.0.0+local
fi
python -m pip install --no-build-isolation .

rm -rf doc/build
python -m sphinx -W -b html doc/source doc/build/html

exec python -m http.server "${PORT:-8000}" \
    --bind 0.0.0.0 \
    --directory doc/build/html
