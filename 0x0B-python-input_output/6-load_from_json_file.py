#!/usr/bin/python3
"""6. Create object from a JSON file TASK"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”

    Args:
        filename: name of the file
    """
    if filename == "":
        return ""

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
