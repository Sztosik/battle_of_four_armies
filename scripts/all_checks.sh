#!/bin/bash
set -Eeuo pipefail

cd "$(dirname "$(readlink -f "$0")")"/..

green_echo() {
    tput setaf 2
    echo "==== $* ===="
    tput sgr0
}

green_echo Checking formatting with black
scripts/formatting_check.sh

green_echo Checking code complexity
scripts/cc_check.sh

green_echo Checking typing with mypy
scripts/mypy_check.sh

green_echo Linting with pylint
scripts/pylint_check.sh

green_echo Running unit tests
scripts/run_tests.sh

green_echo All checks okay!
