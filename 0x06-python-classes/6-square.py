#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Defines a square by its size"""
    def __init__(self, size=0, position=(0, 0)):
        """Defines a new square instance with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property getter for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for position attribute."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a circle"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
