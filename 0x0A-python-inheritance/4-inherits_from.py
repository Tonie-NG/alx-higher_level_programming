#!/usr/bin/python3
"""Defines inherits_from function."""


def inherits_from(obj, a_class):
    """Checks  if the object is an instance of an inherited class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        True if the object is exactly the same or false.
    """
    if issubclass(obj.__class__, a_class) and not isinstance(obj.__class__, a_class):
        return True
    else:
        return False
