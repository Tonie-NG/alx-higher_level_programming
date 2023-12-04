#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        True if the object is exactly the same or false.
    """
    if isinstance(obj, a_class):
        return True
    return False
