#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):


    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class

            Arguments:

                width: width of the rectangle
                height: height of the rectangle
                x: x coordinate of the rectangle
                y: y coordinate of the rectangle
                id: id of the rectangle
        """

        super().__init(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self, value):
        self.__x =value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = vlaue

    @prperty
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            calculates the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            prints the rectangle instance with the # character
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
            prints the string representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}". format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.height)

    def update(self, *args, **kwargs):
        """
            assigns argument to the class attributes
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key = "x":
                    self.__x = value
                if key == "y":
                    self.__y = value


    def to_dictionary(self):
        """
            returns dictionary representation of the rectangle
        """

        return {"x": self.__x,
                "y": self.__y,
                "width": self.__width,
                "height": self.__height,
                "id": self.id
                }
