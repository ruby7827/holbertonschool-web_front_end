#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """A class that defines base geometry."""

    def area(self):
        """Raise an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
