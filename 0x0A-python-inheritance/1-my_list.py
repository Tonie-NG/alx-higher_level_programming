#!usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """A a class MyList that inherits from list."""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))
