#!/usr/bin/python3
for x in range(10):
    for y in range(x+1, 10):
        if y < 9:
            print("{}{}".format(x, y), end=', ')
        else:
            print("{}{}".format(x, y))
