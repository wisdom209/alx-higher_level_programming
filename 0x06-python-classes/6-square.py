#!/usr/bin/python3
"""
A blueprint for square objects
"""


class Square:
    """Square class

    private instance field(s) : size
    methods: __init__, area

    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes the class

        Args:
            size (int, optional): size of square. Defaults to 0.
                        position (tuple, optional): coordinates.
                                                    Defaults to (0,0)
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """`position` getter

        Returns:
            tuple: `position`
        """
        return self.__position

    @position.setter
    def position(self, value):
        """`size` setter

        Args:
            position (tuple): new position
        """
        if (type(value) is tuple
                and len(value) == 2
                and type(value[0]) is int
                and type(value[1]) is int
                and value[0] >= 0
                and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError(
                "position must be a tuple of 2 positive integers")

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
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                if (j == 0):
                    print(" " * self.__position[0], end="")
                print("#", end="")
            print()
