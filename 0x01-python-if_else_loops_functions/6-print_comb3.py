#!/usr/bin/python3
for i in range(88):
    if i % 10 > i // 10:
        print("{}".format(i).zfill(2), ", ", end="", sep="")

print("89", end="\n")
