#!/usr/bin/python3
def read_file(filename=""):
    """function that reads a text file and prints it"""


    with open("my_file_0.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
