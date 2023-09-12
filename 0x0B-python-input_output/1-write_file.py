#!/usr/bin/python3
"""1. Write to a file TASK"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename: reading file's name
        text: string will write in file
    """
    if filename == "" or text == "":
        return 0

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
