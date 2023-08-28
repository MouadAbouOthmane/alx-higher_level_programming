#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    r = 0
    i = 0
    try:
        for itm in my_list:
            i += 1
            if x == r:
                print()
                return r
            if type(itm) == int:
                print("{:d}".format(itm), end="")
                r += 1
        if i < x:
            raise IndexError
        print()
        return r
    except Exception as err:
        raise
