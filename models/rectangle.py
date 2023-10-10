#!/usr/bin/python3
"""Import base moule"""
from models.base import Base

"""
Module Rectangle
"""


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle object """
        return self.width * self.height

    def display(self):
        """Display the Rectangle instance"""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end="")

    def __str__(self):
        """method so that it returns [Rectangle] informations"""
        str_rectangle = "[Rectangle]"
        str_id = " ({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_size = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_x_y + str_size

    def update(self, *args, **kwargs):  # add **kwargs
        """method that assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method that returns dictionary"""
        attr = ['id', 'width', 'height', 'x', 'y']
        dic_attr = {}
        for key in attr:
            dic_attr[key] = getattr(self, key)
        return dic_attr
