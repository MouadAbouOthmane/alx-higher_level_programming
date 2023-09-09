#!/usr/bin/python3
"""Text indentation Module"""


def text_indentation(text):
    """Function that prints a text with 2 new lines.

    Args:
        text: a string
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in text:
        print(c, end="")
        if c in ['.', '?', ':']:
            print()
            print()
