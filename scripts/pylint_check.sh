#!/bin/bash

# Linting is done with pylint, no surprises here
# Configuration is stored in `.pylintrc` and
# the checks fail if code quality fails under 9/10

set -Eeuo pipefail

cd "$(dirname "$(readlink -f "$0")")"/..

git ls-files | grep 'py$' | xargs poetry run pylint --fail-under=9
