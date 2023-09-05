#!/usr/bin/python3
for number in range(99 + 1):
    print("{:02}".format(number), end=", " if number != 99 else "\n")
