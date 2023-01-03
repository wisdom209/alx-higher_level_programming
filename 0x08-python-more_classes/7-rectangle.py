#!/usr/bin/python3
"This module defines a Rectangle class"


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the class

        Args:
            width (int, optional): width. Defaults to 0.
            height (int, optional): height. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter

        Returns:
            int: rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value (int): new width

        Raises:
                        TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (int): height

        Raises:
                        TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to get area of Rectangle

        Returns:
            int: area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Method to get the perimeter of rectangle

        Returns:
            int: Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """returns string representation of class
        NB: Why does self.print_symbol work????

        Returns:
            str: Rectangle string representation
        """
        x = self.__width
        y = self.__height
        new_str = ""

        if x == 0 or y == 0:
            return new_str

        for i in range(y):
            if i == y - 1:
                new_str += str(self.print_symbol) * x
                break
            new_str += str(self.print_symbol) * x + "\n"
        return new_str

    def __repr__(self):
        """returns formal representation of class

        Returns:
            str: formal representation of class
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints bye rectangle when instance deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
