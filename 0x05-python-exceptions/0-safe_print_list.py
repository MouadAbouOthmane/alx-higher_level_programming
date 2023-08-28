#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        if my_list == [] or x < 1:
            return 0
        for i in range(x):
            print(my_list[i], end="")
        print()
        return i + 1
    except IndexError:
        print()
        return i
