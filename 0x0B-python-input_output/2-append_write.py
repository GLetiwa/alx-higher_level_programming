#!/usr/bin/python3
"python append"


def append_write(filename="", text=""):
    "appends a string at end of a file"
    with open(filename, "a", encoding="utf-8") as file:
        num_chars = file.write(text)
    return (num_chars)
