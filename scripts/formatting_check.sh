#!/bin/bash
set -Eeuo pipefail

cd "$(dirname "$(readlink -f "$0")")"/..

git ls-files | grep 'py$' | xargs isort 
git ls-files | grep 'py$' | xargs black

git_output="$(git status --porcelain)"

if [[ -n "${git_output}" ]]; then
  echo "Exiting with non-zero status, because repo is not clean:"
  echo
  git status -s
else
  echo "No changes to the repo were made, exiting with 0"
fi
