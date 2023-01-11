#!/usr/bin/python3
"""
===================================
module with class BaseGeometry
===================================
"""


class BaseGeometry:
    """Basegeometry class"""
    
    @classmethod
    def area(self):
        """For calculating area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a number is integer"""

        if type(value) is not int:
            raise Exception("{} must be an integer".format(name))
        
        if value <= 0:
            raise Exception("{} must be greater than 0".format(name))

