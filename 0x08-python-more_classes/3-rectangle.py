#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents a reactangle."""

    def __init__(self, width=0, height=0):
        """Initialize properties of a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Caculates the area of thed rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Caculates the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

     def __str__(self):
         """Returns a printable rectangular perimeter."""
         if self.__width == 0 or self.__height == 0:
             return ("")
         rect_str = []
         for i in range(self.__height):
             [rect_str.('#') for j in range(self.__width)]
             if i != self.__height - 1:
                 rect_str.append("\n")
         return ("".join(rect_str))
