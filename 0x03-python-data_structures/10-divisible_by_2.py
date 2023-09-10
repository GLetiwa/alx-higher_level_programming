#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            results.append(True)
        else:
            results.append(False)

    return (results)
