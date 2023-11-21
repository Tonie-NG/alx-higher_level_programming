#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Prints and integer

    Args:
        value (int): teh integer to print

    Returns:
        True if it's a valid integer or false if it isn't
    """
    try:
         print("{:d}".format(value))
         return (True)
    except (TypeError, ValueError):
         print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
         return (False)
