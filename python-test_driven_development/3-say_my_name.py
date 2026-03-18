#!/usr/bin/python3
"""This module defines the say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Print My name is first_name last_name.

    Args:
        first_name (str): First name.
        last_name (str): Last name. Default is empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
