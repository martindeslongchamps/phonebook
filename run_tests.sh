#!/usr/bin/env bash

pip3 install Mock
pip3 install Coverage

python3 -m coverage erase
python3 -m coverage run ./unittests/medium_tests.py
python3 -m coverage html
python3 -m coverage xml