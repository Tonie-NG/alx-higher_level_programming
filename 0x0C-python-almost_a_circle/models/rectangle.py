#!/usr/bin/python3

"""A module that defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor to be called on instantiation.

        Args:
            id (int): Unique identifier for the new instance.
            width (int): rectangle width.
            height (int): rectangle height.
            x (int): x coordinate of the rectangle.
            y (int): y coordinate of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value_width):
        if type(value_width) != int:
            raise TypeError("width must be an integer")
        if value_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value_width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value_height):
        if type(value_height) != int:
            raise TypeError("height must be an integer")
        if value_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value_height

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value_x):
        if type(value_x) != int:
            raise TypeError("x must be an integer")
        if value_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value_x

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value_y):
        if type(value_y) != int:
            raise TypeError("y must be an integer")
        if value_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value_y

    def area(self):
        """Returns the area of the Rectangle instance."""
        val = self.height * self.width
        return val

    def display(self):
        """print in stdout the Rectangle instance with the character #."""
        [print("") for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            for w in range(self.__width):
                print("{}".format('#'), end="")
            print("")

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates a rectangle instance

        Args:
            *args (ints): An ordered representation of new attribute values.
            **kwargs (dict): A key value pair of the new attributes.
        """
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if index == 1:
                    self.width = arg
                if index == 2:
                    self.height = arg
                if index == 3:
                    self.x = arg
                if index == 4:
                    self.y = arg
                index += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
