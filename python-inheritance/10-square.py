#!/usr/bin/python3
"""This module defines the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
