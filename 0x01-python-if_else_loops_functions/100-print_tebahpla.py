#!/usr/bin/python3
for c in range(122, 96, -1):
    if not(c % 2 == 0):
        print("{}".format(chr(c).upper()), end="")
    else:
        print("{}".format(chr(c)), end="")
