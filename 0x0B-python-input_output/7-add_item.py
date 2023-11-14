#!/usr/bin/python3
"""Add arguments to Python list and save them to a file"""


import sys


r = __import__('6-load_from_json_file').load_from_json_file
w = __import__('5-save_to_json_file').save_to_json_file


def json_append(filename):
    """adds args to a Python list, and saves the file"""
    try:
        content = r(filename)
    except FileNotFoundError:
        content = []
    for i in sys.argv[1:]:
        content.append(i)
    w(content, filename)


def main():
    """the main function"""
    filename = 'add_item.json'
    json_append(filename)


if __name__ == "__main__":
    main()
