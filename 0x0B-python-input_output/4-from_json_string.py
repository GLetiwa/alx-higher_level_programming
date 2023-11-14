#!/usr/bin/python3
"python json"


import json


def from_json_string(my_str):
    """returns an object represented by JSON string"""
    data = json.loads(my_str)
    return (data)
