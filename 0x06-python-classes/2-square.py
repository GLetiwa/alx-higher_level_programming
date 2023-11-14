#!/usr/bin/python3
"""Defines a square"""


class Square:
    """

    Defines a square by its size

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """

        Initializes a square instance with optional size.


        Args:
            size (int, optional): The size of the square.

        Raises:
            TypeError: If size is not an int
            ValueError: If size is less than 0


        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
