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

    def area(self):
        """Get area of square instance

        Returns:
            int: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # symbol
        """
        if (self.__size == 0):
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
