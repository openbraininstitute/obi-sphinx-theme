#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
IMAGE_NAME=${IMAGE_NAME:-obi-sphinx-theme-rtd}
PORT=${PORT:-8000}

cd "${ROOT_DIR}"
podman build --tag "${IMAGE_NAME}" --file Containerfile.rtd .
printf 'RTD preview: http://localhost:%s/\n' "${PORT}"
exec podman run --rm \
    --name "${IMAGE_NAME}" \
    --publish "127.0.0.1:${PORT}:8000" \
    --volume "${ROOT_DIR}:/src:ro" \
    "${IMAGE_NAME}"
