#!/usr/bin/python3
import sys
import os

os.write(2, bytearray("and that piece of art is useful - Dora Korpar, 2015-10-19\n", encoding="UTF-8", errors="e"))
sys.exit(1)