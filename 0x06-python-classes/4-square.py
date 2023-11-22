#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """A Square class."""

    def __init__(self, size=0):
        """Initializes attributes of a square class

        Args:
            size (int): The size of the new square.
        """
        self.size = size
    
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the sqaure

        Returns:
            the area of the square.
        """
        area = self.__size * self.__size
        return (area)
