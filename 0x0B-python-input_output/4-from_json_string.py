#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a from_json_string function."""
import json


def from_json_string(my_str):
    """Rreturns an object represented by a JSON string."""
    return json.loads(my_str)
