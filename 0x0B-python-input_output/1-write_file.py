#!/usr/bin/python3
"python write"


def write_file(filename="", text=""):
    "writes a string to a text file"
    with open(filename, "w", encoding="utf-8") as file:
        num_chars = file.write(text)
        return (num_chars)
