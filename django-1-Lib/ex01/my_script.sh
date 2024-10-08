#!/bin/bash

python3 -m pip -V
python3 -m pip install -t local_lib --upgrade path --log pip-install.log
python3 my_program.py
