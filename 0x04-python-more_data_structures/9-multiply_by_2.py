#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dc = a_dictionary.copy()
    list_keys = list(new_dc.keys())

    for i in list_keys:
        new_dc[i] *= 2
    return (new_dc)
