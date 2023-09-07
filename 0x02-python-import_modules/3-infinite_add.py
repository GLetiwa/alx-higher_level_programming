#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = len(sys.argv) - 1
    total = 0
    for i in range(1, args + 1):
        argument = sys.argv[i]
        total += int(argument)
    print("{}".format(total))
