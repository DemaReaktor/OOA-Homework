class Rational:
    """rational number"""
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int):
            raise TypeError('type of numerator should be "int"')
        if not isinstance(denominator, int):
            raise TypeError('type of denominator should be "int"')
        if not denominator:
            raise ValueError("denominator must not be 0")
        self.__sign = numerator*denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        self.__numerator = numerator//Rational.nsd(numerator, denominator)
        self.__denominator = denominator//Rational.nsd(numerator, denominator)

    def __str__(self):
        if self.__sign:
            return '-'+str(self.__numerator) + '/' + str(self.__denominator)
        else:
            return str(self.__numerator) + '/' + str(self.__denominator)

    def __float__(self):
        return self.__numerator/self.__denominator*(-1. if self.__sign else 1.)

    @classmethod
    def nsd(cls, a, b):
        """find the least common divisor of b and a"""
        if a == 0 or b == 0:
            return 1
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a


a = Rational(3, 26)
b = Rational(6, 2)
c = Rational(9, -1)
print(a, b, c)
print(float(a), float(b), float(c))
