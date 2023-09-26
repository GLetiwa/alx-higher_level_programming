#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Defines a square by its size"""
    def __init__(self, size=0):
        """Defines a new square instance with optional size."""
        self.__size = size

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

    def area(self):
        """Calculates the area of a circle"""
        return self.__size ** 2
