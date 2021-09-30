class Rectangle:
    def __init__(self, width=1., length=1.):
        self.__width = (width if width < 20. else 20.) if width > 0. else 0.
        self.__length = (length if length < 20. else 20.) if length > 0. else 0.

    def perimetr(self):
        return 2.*(self.__width+self.__length)

    def square(self):
        return self.__width*self.__length

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    def set_width(self, width):
        self.__width = (width if width < 20. else 20.) if width > 0. else 0.

    def set_length(self, length):
        self.__length = (length if length < 20. else 20.) if length > 0. else 0.


x = Rectangle(3, 26)
print(x.square(), ' ', x.perimetr())