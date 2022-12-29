#!/usr/bin/python3
for i in range(100):
    print(f"{i}".zfill(2), end="")
    if i != 99:
        print(", ", end="")
