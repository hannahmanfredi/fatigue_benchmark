#!/bin/bash
# This script will set up a Pipenv environment with Python 3.11, install specific versions of ipykernel and python-dotenv, and set up an IPython kernel named "fatigue_benchmark".

set -e

pipenv --python 3.11
pipenv install ipykernel==6.28.0 python-dotenv==1.0.0
pipenv run python -m ipykernel install --user --name="fatigue_benchmark" --display-name="fatigue_benchmark"
pipenv install