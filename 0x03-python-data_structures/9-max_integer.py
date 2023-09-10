#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_int = my_list[0]
    for num in range(len(my_list)):
        if my_list[num] > max_int:
            max_int = my_lis[num]

    return (max_int)
