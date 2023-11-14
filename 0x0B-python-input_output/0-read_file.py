#!/usr/bin/python3
"Python I/O"


def read_file(filename=""):
    "Reads a text file and prints to stdout"
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
