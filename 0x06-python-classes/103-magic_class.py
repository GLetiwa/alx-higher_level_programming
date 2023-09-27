#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided."""

import math


class MagicClass:
    """Defines a circle."""
    def __init__(self, radius):
        """Check if radius is a number (int or float)"""
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """Return the area of the MagicClass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the MagicClass"""
        return 2 * math.pi * self.__radius
