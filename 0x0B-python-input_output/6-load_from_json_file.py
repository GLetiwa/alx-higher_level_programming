#!/usr/bin/python3
"""python json"""


import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename, "r") as file:
        data = json.load(file)
        return data
