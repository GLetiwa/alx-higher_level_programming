#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        element = 0
        for i in my_list:
            if element < x:
                print(i, end="")
                element += 1
        print()
        return (element)
    except TypeError:
        print("Invalid input")
        return (0)
