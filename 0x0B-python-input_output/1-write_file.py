#!/usr/bin/python3


def write_file(my_first_file="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters"""
    with open("my_first_file.txt", "w", encoding="UTF-8") as f:
        return f.write(text)
