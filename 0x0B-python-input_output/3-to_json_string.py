#!/usr/bin/python3
"""3. To JSON string TASK"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)

    Args:
        my_obj: converted object
    """
    json_string = json.dumps(my_obj, skipkeys=True, sort_keys=True)
    return json_string
