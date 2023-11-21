#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the result.
    Args:
        a (int):  numerator
        b (int): denominator

    Returns:
        the result of the division or None on error
    """
    try:
        c = a/b
    except (TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return (c)
