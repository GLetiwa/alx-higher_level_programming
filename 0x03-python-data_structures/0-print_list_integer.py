#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        if not my_list:
            return
        for i in my_list:
            print("{:d}".format(i))
