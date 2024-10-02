#!/bin/bash

python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirement.txt
python3 ./app/manage.py runserver 0.0.0.0:8000
