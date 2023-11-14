#!/usr/bin/python3
def raise_exception():
    try:
        result = 1 + '2'
    except TypeError as e:
        raise e
