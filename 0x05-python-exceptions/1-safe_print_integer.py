#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer

    Args:
        value (any): The value to print

    Return:
        True if teh value is an integer.
        False on error (TypeError or ValueError)
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
