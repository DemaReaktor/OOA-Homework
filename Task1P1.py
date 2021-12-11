class Rational:
    """rational number"""
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int):
            raise TypeError('type of numerator should be "int"')
        if not isinstance(denominator, int):
            raise TypeError('type of denominator should be "int"')
        if not denominator:
            raise ValueError("denominator must not be 0")
        self.__sign = -1 if numerator*denominator < 0 else 1
        numerator = abs(numerator)
        denominator = abs(denominator)
        self.__numerator = numerator//Rational.nsd(numerator, denominator)
        self.__denominator = denominator//Rational.nsd(numerator, denominator)

    def __str__(self):
        if self.__sign == -1:
            return '-'+str(self.__numerator) + '/' + str(self.__denominator)
        else:
            return str(self.__numerator) + '/' + str(self.__denominator)

    def __float__(self):
        return self.__numerator/self.__denominator*self.__sign

    def __call__(self):
        return self.__sign*self.__numerator/self.__denominator

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be added')
        if not other:
            raise ValueError('value should be not None')
        denominator = self.__denominator*other.__denominator
        numerator = self.__numerator*self.__sign*other.__denominator + \
            other.__numerator*other.__sign*self.__denominator
        self.__sign = -1 if numerator < 0 else 1
        numerator *= self.__sign
        nsd = Rational.nsd(numerator, denominator)
        self.__numerator, self.__denominator = numerator//nsd, denominator//nsd
        return self

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be subtracted')
        if not other:
            raise ValueError('value should be not None')
        denominator = self.__denominator * other.__denominator
        numerator = self.__numerator * self.__sign * other.__denominator - \
            other.__numerator * other.__sign * self.__denominator
        self.__sign = -1 if numerator < 0 else 1
        numerator *= self.__sign
        nsd = Rational.nsd(numerator, denominator)
        self.__numerator, self.__denominator = numerator // nsd, denominator // nsd
        return self

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be multiplied')
        if not other:
            raise ValueError('value should be not None')
        denominator = self.__denominator * other.__denominator
        numerator = self.__numerator * other.__numerator
        self.__sign *= other.__sign
        nsd = Rational.nsd(numerator, denominator)
        self.__numerator, self.__denominator = numerator // nsd, denominator // nsd
        return self

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be divided')
        if not other:
            raise ValueError('value should be not None')
        if not other.__numerator:
            raise ZeroDivisionError('numerator of rational should not be 0')
        denominator = self.__denominator * other.__numerator
        numerator = self.__numerator * other.__denominator
        self.__sign *= other.__sign
        nsd = Rational.nsd(numerator, denominator)
        self.__numerator, self.__denominator = numerator // nsd, denominator // nsd
        return self

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be equaled')
        if not other:
            raise ValueError('value should be not None')
        return self.__sign*self.__numerator*other.__denominator < \
            other.__sign*other.__numerator*self.__denominator

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be equaled')
        if not other:
            raise ValueError('value should be not None')
        return self.__sign*self.__numerator*other.__denominator <= \
            other.__sign*other.__numerator*self.__denominator

    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be equaled')
        if not other:
            raise ValueError('value should be not None')
        return self.__sign*self.__numerator*other.__denominator >= \
            other.__sign*other.__numerator*self.__denominator

    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be equaled')
        if not other:
            raise ValueError('value should be not None')
        return self.__sign*self.__numerator*other.__denominator > \
            other.__sign*other.__numerator*self.__denominator

    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('only values of type Rational can be equaled')
        if not other:
            raise ValueError('value should be not None')
        return self.__sign == other.__sign and other.__denominator == \
            self.__denominator and self.__numerator == other.__numerator

    def __ne__(self, other):
        return not self == other

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
c = Rational(6, 2)
print(a, b, c)
print(float(a), float(b), float(c), a >= b, a <= b, a <= c, a >= c, b != c, b >= c, a())
