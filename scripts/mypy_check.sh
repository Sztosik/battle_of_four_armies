#!/bin/bash

# Type checking is done by mypy
# https://github.com/python/mypy
# currently using the default settings,
# although there are some extra strict
# checks that can be enabled in the future
# Refer to `mypy --help`

set -Eeuo pipefail
cd "$(dirname "$(readlink -f "$0")")"/..

poetry run mypy -p drone --namespace-packages
