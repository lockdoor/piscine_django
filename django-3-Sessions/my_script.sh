#!/bin/bash

python3 -m venv ~/venv/$PWD
. ~/venv/$PWD/bin/activate
pip install --upgrade pip
pip install -r requirement.txt
python3 manage.py runserver 0.0.0.0:8000
