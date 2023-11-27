#!/usr/bin/python3

"""Defines a rectangle class."""


class Rectangle:
    """Represents a reactangle."""

    def __init__(self, width=0, height=0):
        """Initialize properties of a new rectangle

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height  of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

