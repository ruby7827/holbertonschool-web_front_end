#!/usr/bin/python3
"""This module defines the CountedIterator class."""


class CountedIterator:
    """A class that extends the built-in iterator with a counter."""

    def __init__(self, iterable):
        """Initialize a new CountedIterator.

        Args:
            iterable: The iterable to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated."""
        return self.count

    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item
