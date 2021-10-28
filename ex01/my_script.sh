#!/bin/sh

pip3 -V
rm -rf local_lib > path_install.log 2>>path_install.log
pip3 install git+https://github.com/jaraco/path.git -t ./local_lib >> path_install.log 2>>path_install.log
python3 my_program.py
