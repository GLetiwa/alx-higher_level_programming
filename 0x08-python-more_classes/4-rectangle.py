#!/usr/bin/python3
"""Function defines a rectangle"""


class Rectangle:
    """defines attributes of the class"""
    def __init__(self, width=0, height=0):
        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return a printable representation of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        new = []
        for i in range(self.__height):
            [new.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                new.append("\n")
        return ("".join(new))

    def __repr__(self):
        """Return string representation of a rectangle"""
        new = "Rectangle(" + str(self.__width)
        new += ", " + str(self.__height) + ")"
        return (new)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
