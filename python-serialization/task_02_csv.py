#!/usr/bin/python3
"""This module defines the convert_csv_to_json function."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON format and save to data.json."""
    try:
        with open(csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return True
    except Exception:
        return False
