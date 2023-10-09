#!/usr/bin/python3
"""Lists available attributes"""


def lookup(obj):
    """lists available attributes and methods of an object"""
    list = dir(obj)
    return list
