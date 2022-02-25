#!/usr/bin/python3
# -*- coding=utf-8 -*-
# author:   RedLeaves
# date:     2022/02/25
# version:  1.0


import subprocess
import os


def main():
    uis = []

    for root, dirs, files in os.walk("ui"):
        for file in files:
            if ".ui" in file:
                uis.append(os.path.join(root, file))

    for ui in uis:
        subprocess.call("pyside6-uic %s -o %s.py" % (ui, ui.split(".")[0]), shell=True)


if __name__ == "__main__":
    main()
