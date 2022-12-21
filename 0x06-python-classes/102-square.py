#!/usr/bin/python3
"""
A blueprint for square objects
"""


class Square:
    """Square class

    private instance field(s) : size
    methods: __init__, area

    """

    def __init__(self, size=0):
        """initializes the class

        Args:
            size (int, optional): size of square. Defaults to 0.
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Get area of square instance

        Returns:
            int: area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """`size` getter

        Returns:
            int: `size`
        """
        return self.__size

    @size.setter
    def size(self, value):
        """`size` setter

        Args:
            value (int): new size
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, object):
        """checks equality of areas

        Args:
            object (Square): other square area

        Returns:
            Boolean: True
        """
        return self.__size ** 2 == object.__size ** 2

    def __ne__(self, object):
        """checks if areas are not equal

        Args:
            object (Square): other square area

        Returns:
            Boolean: True
        """
        return self.__size ** 2 != object.__size ** 2

    def __gt__(self, object):
        """checks if area is greater than other area

        Args:
            object (Square): other square area

        Returns:
            Boolean: True
        """
        return self.__size ** 2 > object.__size ** 2

    def __ge__(self, object):
        """checks if area is greater than or equal other area

        Args:
            object (Square): other square area

        Returns:
            Boolean: True
        """
        return self.__size ** 2 >= object.__size ** 2

    def __lt__(self, object):
        """checks if area is less than other area

        Args:
            object (Square): other square area

        Returns:
            Boolean: True
        """
        return self.__size ** 2 < object.__size ** 2

    def __le__(self, object):
        """checks if area is less than or equal other area

        Args:
            object (Square): other square area

        Returns:
            Boolean: True
        """
        return self.__size ** 2 <= object.__size ** 2
