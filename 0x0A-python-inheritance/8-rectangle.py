#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
============================
Module for Rectangle Class
============================
"""


class Rectangle(BaseGeometry):
    """Rectangle class is a subclass of BaseGrometry"""

    def __init__(self, width, height):

        self.integer_validator("width", width)
            self.__width = width

        self.integer_validator("height", height)
            self.height = height
