#!/usr/bin/python3


def class_to_json(obj):
    """
    Function that returns the dictionary
    description with simple data structure

    Args:
        obj: instance of class
    """
    if not obj:
        return
    return vars(obj)
