#!/usr/bin/env bash
set -e

black -l 120 .
isort -rc .
mypy .
flake8 .
