#!/usr/bin/python3
i = 0
for c in range(122, 64, -1):
    if c % 2 == 0:
        i = 32
    else:
        i = 0
    print("{}".format(chr(c - i)), end='')
