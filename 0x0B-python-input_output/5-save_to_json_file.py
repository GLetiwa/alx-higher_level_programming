#!/usr/bin/python3
"python JSON"


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON rep"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
