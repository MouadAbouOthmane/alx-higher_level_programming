#!/usr/bin/python3
"""4. From JSON string to Object TASK"""
import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: a json string
    """
    my_obj = json.loads(my_str)
    return my_obj
