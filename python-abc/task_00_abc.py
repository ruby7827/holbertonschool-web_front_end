#!/usr/bin/python3
"""This module defines the Animal, Dog and Cat classes."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract class that defines an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """A class that defines a dog."""

    def sound(self):
        """Return the sound of the dog."""
        return "Bark"


class Cat(Animal):
    """A class that defines a cat."""

    def sound(self):
        """Return the sound of the cat."""
        return "Meow"
