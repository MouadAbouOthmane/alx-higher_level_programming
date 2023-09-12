#!/usr/bin/python3
"""0. Read file Module"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: reading file's name
    """
    if filename == "":
        return

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())

read_file("my_file_0.txt")