#!/usr/bin/env bash
set -e  # exit script if any command fails
set -x  # echo all commands

# create venv for src
cd src
python3.11 -m poetry config virtualenvs.in-project true
python3.11 -m poetry install