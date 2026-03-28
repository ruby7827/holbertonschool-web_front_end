#!/usr/bin/python3
"""This module defines the write_file function."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
