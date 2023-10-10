#!/usr/bin/python3
"""python file I/O"""


def append_after(filename="", search_string="", new_string=""):
    """inserts line to a text file"""
    test = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
