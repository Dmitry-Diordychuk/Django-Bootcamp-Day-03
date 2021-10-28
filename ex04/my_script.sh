#!/bin/sh

python3 -m venv ./django_venv
source ./django_venv/bin/activate
echo $PWD
pip3 install -U pip setuptools
pip3 install -r requirement.txt
