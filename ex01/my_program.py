#!/usr/bin/python3
# coding: utf-8
from local_lib.path import Path


def run():
    try:
        d = Path("./path")
        d.mkdir_p()
        d /= "file"
        d.touch()
        d.write_text("Hello, world!\n")
        print(d.read_text())
    except Exception as ex:
        raise ex


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        print("Error:", ex)
