#!/usr/bin/env python3

def no_c(my_string):
    """
    A function that removes all occurrence oif C from a string
    """
    new_string = ""
    for char in my_string:
        if char != "c" or char != "C":
            new_string += char
    return new_string

