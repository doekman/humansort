#!/usr/bin/env bash
# Unofficial Bash Strict Mode
set -euo pipefail
IFS=$'\n\t'

T="$(mktemp -t actual-)"

echo "# TESTING: 1_basic"
../humansort.py < 1_basic/input.txt > $T; diff --brief "$T" 1_basic/expected.txt

rm "$T"