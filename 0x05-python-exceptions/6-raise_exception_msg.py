#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        1 + '2'
    except TypeError:
        raise TypeError(message)
