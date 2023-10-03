#!/usr/bin/python3
"""defines locked class"""


class LockedClass:
    """prevents user from instantiating attributes that are not first name"""
    __slots__ = ["first_name"]
