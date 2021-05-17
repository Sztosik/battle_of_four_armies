#!/bin/bash

# 2 tools are being used to calculate and monitor 
# code's cyclomatic complexity: xenon and radom.
# Radon provides a nice breakdown of the 
# complexity of functions and classes.
# Xenon allows to define complexity limits,
# which will cause the script to fail
# when they're exceeded. This CI check
# is experimental. We'll see if its 
# of any usefulness in the future :)

set -Eeuo pipefail

cd "$(dirname "$(readlink -f "$0")")"/..

git ls-files | grep 'py$' | xargs poetry run radon cc # Print complexity info
git ls-files | grep 'py$' | xargs poetry run xenon --max-absolute C --max-modules A --max-average A # Fail if complexity too high
