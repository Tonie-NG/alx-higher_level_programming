#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """A class MyList that inherits from list."""

    def print_sorted(self):
        """Print a list in ascending order."""
        print(sorted(self))
