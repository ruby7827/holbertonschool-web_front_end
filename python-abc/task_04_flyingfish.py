#!/usr/bin/python3
"""This module defines Fish, Bird and FlyingFish classes."""


class Fish:
    """A class that defines a fish."""

    def swim(self):
        """Print swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat message."""
        print("The fish lives in water")


class Bird:
    """A class that defines a bird."""

    def fly(self):
        """Print flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class that defines a flying fish."""

    def swim(self):
        """Print swimming message."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print flying message."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print habitat message."""
        print("The flying fish lives both in water and the sky!")
