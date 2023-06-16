#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Create an instance of class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes Square
        Atributtes:
            size: size of square
            position: blanks spaces before the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter
        Return:
            size of square
        """
        return self.__size

    @property
    def position(self):
        """
        getter
        Return:
            position to start print square
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        setter
        atributtes:
            value, the new size
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        """
        setter
        atributtes:
            value, the new position
        """
        self.__position = value
        if type(value) is not tuple or len(value) != 2 \
           or type(value[0]) is not int or type(value[1]) is not int \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Public instance method
        Return:
            the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        print to square made of #
        """
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                for i in range(self.position[1]):
                    print()
            for column in range(self.size):
                for lines in range(self.position[0]):
                    print(" ", end="")
                for row in range(self.size):
                    print("#", end="")
                print()
