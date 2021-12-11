class Good:
    def __init__(self, name, price):
        if not isinstance(name, str):
            raise TypeError('name should have type "str"')
        if not isinstance(price, float):
            raise TypeError('price should have type "float"')
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return 'name: '+self.__name+', price: '+str(self.__price)


class Composition:
    """a class which have information about goods in a composition"""
    def __init__(self):
        self.__goods_count = {}

    @property
    def catalog(self):
        return self.__goods_count.keys()

    def get_count(self, good):
        """return count of good in composition"""
        if not isinstance(good, Good):
            raise TypeError('good should have type "Good"')
        return self.__goods_count[good]


    def __iadd__(self, other):
        if not isinstance(other, dict):
            return NotImplemented
        for key in other.keys():
            if not isinstance(key, Good) or not isinstance(other[key], int):
                return NotImplemented
            if not(key in self.__goods_count):
                if other[key] < 0:
                    raise ValueError('there are not so much goods in composition')
                self.__goods_count[key] = other[key]
            else:
                if -other[key] > self.__goods_count[key]:
                    raise ValueError('there are not so much goods in composition')
                self.__goods_count[key] += other[key]
            if not self.__goods_count[key]:
                self.__goods_count.pop(key)
        return self

    def __isub__(self, other):
        if not isinstance(other, dict):
            return NotImplemented
        for key in other.keys():
            if not isinstance(key, Good) or not isinstance(other[key], int):
                return NotImplemented
            if not(key in self.__goods_count):
                if other[key] > 0:
                    raise ValueError('there are not so much goods in composition')
            else:
                if other[key] > self.__goods_count[key]:
                    raise ValueError('there are not so much goods in composition')
            self.__goods_count[key] -= other[key]
            if not self.__goods_count[key]:
                self.__goods_count.pop(key)
        return self

    def __str__(self):
        menu = '{\n'
        for element in self.__goods_count.keys():
            menu += str(element) + ', count: ' + str(self.__goods_count[element]) + ';\n'
        return menu + '}'


x = Composition()
x += {Good('1', 10.): 10, Good('2', 10.): 90, Good('3', 15.): 110}
print(x)
