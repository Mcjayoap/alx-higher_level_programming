#!/usr/bin/python3
""" Defines a class that inherits from another class """

class list:
    def __init__(self, MyList = []):
        self.MyList = MyList

class MyList(list):
    """ implement sorted printing of the built-in list class """

    def print_sorted(self):
        """ class MyList that inherits from list """
        print(sorted(self))
