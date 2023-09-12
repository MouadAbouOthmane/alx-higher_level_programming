#!/usr/bin/python3
"""5. Save Object to a file TASK"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file
    using a JSON representation

    Args:
        filename: reading file's name
        my_obj: object will wrote in file
    """
    if filename == "" or my_obj == "":
        return

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
