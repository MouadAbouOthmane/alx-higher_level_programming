#!/usr/bin/python3
"""2. Append to a file TASK"""


def append_write(filename="", text=""):
    """
    function that  appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename: reading file's name
        text: string will write in file
    """
    if filename == "" or text == "":
        return 0

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
