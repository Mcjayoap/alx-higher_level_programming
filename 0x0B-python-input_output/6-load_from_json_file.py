#!/usr/bin/python3
"""creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return jason.load(f)
