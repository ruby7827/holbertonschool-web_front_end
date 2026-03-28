#!/usr/bin/python3
"""This module defines the Student class."""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of a Student."""
        return self.__dict__
