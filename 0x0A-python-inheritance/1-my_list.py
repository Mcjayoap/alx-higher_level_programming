#!/usr/bin/python3
""" Defines a class that inherits from another class """


class MyList(list):
    """
    Implement sorted printing of the 
    built-in list class 
    """
    pass

    def print_sorted(self):
        """ class MyList that inherits from list """
        
        print(sorted(self))
