#!/usr/bin/python3
"""Defines write_file."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8).

    Args:
        filename (str): Name of the file to write to.
        text (str): Text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
