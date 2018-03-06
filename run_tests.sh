#!/bin/bash

python -m unittest discover -v -s binary_search_tree -p "test_*.py"
python -m unittest discover -v -s icake -p "test_*.py"

