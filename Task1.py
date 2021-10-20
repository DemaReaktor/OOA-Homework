class Rectangle:
    """a figure"""
    def __init__(self, width=1., length=1.):
        self.__width = width
        self.__length = length

    def perimeter(self):
        """return the perimeter"""
        return 2.*(self.__width+self.__length)

    def square(self):
        """return the square"""
        return self.__width*self.__length

    def __setattr__(self, key, value):
        if key != '_Rectangle__width' and key != '_Rectangle__length':
            raise AttributeError(f'class does not have attribute "{key}"')
        if not isinstance(value, float):
            raise TypeError(f'type of {key} should be "float')
        if value <= 0 or value >= 20:
            raise ValueError("__length should be in range (0...20)")
        self.__dict__[key] = value


x = Rectangle(3., 6.)
print(x.square(), x.perimeter())
