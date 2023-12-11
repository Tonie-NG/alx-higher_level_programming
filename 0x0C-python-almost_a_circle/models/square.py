#!/usr/bin/python3

"""A module that defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor to be called on instantiation.

        Args:
            id (int): Unique identifier for the new instance.
            width (int): square size (height and width).
            x (int): x coordinate of the square.
            y (int): y coordinate of the sqaure.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/get the width of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates a square instance.

        Args:
            *args (ints): An ordered representation of new attribute values.
            **kwargs (dict): A key value pair of the new attributes.
        """
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle."""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.height,
            "y": self.y
        }

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

