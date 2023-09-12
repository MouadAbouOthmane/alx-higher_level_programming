#!/usr/bin/python3
"""7. Load, add, save TASK"""
import json
import sys
from os.path import isfile


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """
    Script that adds all arguments to a Python list,
    and then save them to a file:
    """

    argv = sys.argv[1:]

    if isfile("./add_item.json"):
        load = load_from_json_file('add_item.json')

        if len(argv) > 0:
            load.extend(argv)
            save_to_json_file(load, 'add_item.json')
    else:
        with open('add_item.json', 'w', encoding="utf-8") as file:
            json.dump(argv, file)


if __name__ == '__main__':
    main()
