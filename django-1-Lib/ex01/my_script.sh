#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
cat << eof > requirement.txt
path==17.0.0
eof
pip install -q -r requirement.txt
rm requirement.txt
python3 my_program.py
deactivate
