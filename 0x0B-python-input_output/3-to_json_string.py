#!/usr/bin/python3
"python json"


import json


def to_json_string(my_obj):
    "returns JSON representation of object(string)"
    json_string = json.dumps(my_obj)
    return (json_string)
