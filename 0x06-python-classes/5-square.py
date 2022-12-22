#!/usr/bin/python3
bdbaraban
/
holbertonschool-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
holbertonschool-higher_level_programming/0x06-python-classes/5-square.py
@234761
234761 Fix usage of properties and improve documentation
 1 contributor
Executable File  41 lines (33 sloc)  1.03 KB
#!/usr/bin/python3
# 5-square.py
# Brennan D Baraban <375@holbertonschool.com>
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
