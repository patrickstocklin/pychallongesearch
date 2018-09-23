#!/bin/bash
#Runs suite of unit tests for us with fail-fast, verbosity, matching all files that end with *test.py
echo "Running Unit Tests..."
python -m unittest discover -f -v -s pychallongesearch/tests/ -p '*test.py'