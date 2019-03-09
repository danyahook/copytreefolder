#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os
import codecs

try:
    folder = codecs.open("bf.txt", mode='r', encoding="windows-1251",  errors="replace")
    fromDirectory = folder.readline()
    folder.close()

    print(fromDirectory)

    toDirectory = os.getcwd() + "\\to"

    try:
        shutil.copytree(fromDirectory, toDirectory)
        error = codecs.open(os.getcwd() + "\\bl.txt", mode='w')
        error.write("successfully")
        error.close()

    except:
        error = codecs.open(os.getcwd() + "\\bl.txt", mode='w')
        error.write("the system cannot find the path specified")
        error.close()

except Exception as e:
    error = codecs.open(os.getcwd() + "\\bl.txt", mode='w')
    error.write(str(e))
    error.close()
