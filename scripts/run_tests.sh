#!/bin/bash
set -Eeuo pipefail

cd "$(dirname "$(readlink -f "$0")")"/..

poetry run python -m pytest --junitxml=.test_result.xml 

