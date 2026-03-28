#!/usr/bin/python3
"""This module defines serialization and deserialization functions."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
