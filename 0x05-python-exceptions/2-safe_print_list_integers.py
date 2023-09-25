#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        elements = 0
        for i in my_list:
            if elements < x and isinstance(i, int):
                print("{:d}".format(i), end="")
                elements += 1
        print()
        return (elements)
    except TypeError:
        return (0)
