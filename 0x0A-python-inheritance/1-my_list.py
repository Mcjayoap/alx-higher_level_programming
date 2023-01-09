#!/usr/bin/python3
""" Defines a class that inheruts from another class """


class MyList(list):
    """ implement sorted printing of the built-in list class """


    def print_sorted(self):
        """ class MyList that inherits from list """
        print(sorted(self))
