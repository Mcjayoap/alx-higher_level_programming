#!/usr/bin/python
"""writes an Object to a text file, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
