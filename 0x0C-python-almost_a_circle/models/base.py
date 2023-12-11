#!/usr/bin/python3

"""Module that defines a base class model."""
import json
import csv
import turtle


class Base:
    """Base Model.

    This represents a model that includes starter methods
    for other models (like the rectangle and square).

    Private Class Attribute:
        __nb_objects (int): Keeps count of the number of instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor to be called on instantiation.

        Args:
            id (int): Unique identifier for the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string representation of list_dictionaries.

        Args:
            list_dictionaries (list): is a list of dictionaries.
        Returns:
            If list_dictionaries is None or empty, "[]".
            Otherwise the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Serializes a list of objects and wriets it to a file.

        Args:
            list_objs (list): s a list of instances who inherits of Base.
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): a string representing a list of dictionaries
        Returns:
            The list of the JSON string representation json_string.
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the class.

        Args:
            **dictionary (dict): dictionary of values to initialize
        Returns:
            An instance with all attributes already set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instances from a json file.
        Reads from `<cls.__name__>.json`.

        Returns:
            An emptylist is the file does not exists
            Else a list of the instantiated objects
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as file:
                list_dict = Base.from_json_string(file.read())
                return [cls.create(**dictionary) for dictionary in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a serialized list of objects to a file.

        Args:
            list_objs (list): A list of classes that inherit the base class.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes deserialized from a csv file

        Reads from `<cls.__name__>.csv`.

        Returns:
            An emptylist if teh file does not exist
            A list of items or instantiated objects
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Utilizes the turtle module to produce
        a graphical representation of objects.

        Args:
            list_rectangles (list): A list of rectangle objects.
            list_squares (list): A list of square objects.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#1aa4b8")
        turt.pensize(4)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rectangle in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for i in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#808080")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
