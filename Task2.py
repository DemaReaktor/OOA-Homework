from operator import *

class Rational:
    def __init__(self, numerator=1, denominator=1):
        # self.sign = numerator < 0 ^ denominator < 0
        self.__numerator = int(abs(numerator)/nsd(numerator, denominator))
        self.__denominator = int(denominator/nsd(numerator, denominator))

    def __str__(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    def __float__(self):
        try:
            return float(self.__numerator)/self.__denominator
        except:
            return 0.

def nsd(a, b):
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
c = Rational(9, 0)
print(a, b, c)
print(float(a), float(b), float(c))
