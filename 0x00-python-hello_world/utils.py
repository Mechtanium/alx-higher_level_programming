#!/usr/bin/python3
import py_compile
import sys

PYFILE = str(sys.argv[1])
py_compile.compile(PYFILE, cfile=f"{PYFILE}c")
