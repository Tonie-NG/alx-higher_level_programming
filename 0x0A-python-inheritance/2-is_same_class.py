#!/usr/bin/python3
"""Defines is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.
    Args:
        obj (any): The object to check..
        a_class (type): The class to check against.

    Returns:
        True if teh object is exactly the same or false.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
