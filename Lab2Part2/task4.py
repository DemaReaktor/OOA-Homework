class Binary_Tree:
    """element of binary tree"""
    def __init__(self, id, price):
        if not isinstance(id, int):
            raise TypeError("type of id should be 'int'")
        if id <= 0:
            raise ValueError("id should be >0")
        self.price = price
        self.__left = self.__right = None
        self.__id = id

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("type of price should be 'float'")
        if value <= 0:
            raise ValueError("price should be >0")
        self.__price = value

    def add(self, element):
        """
        add a new element
        sort into left branches with less id
        """
        if not isinstance(element, Binary_Tree):
            raise TypeError("type of element should be 'Binary_Tree'")
        # if not element:
        #     raise ValueError("element should be not 'null'")
        if element.__id == self.__id:
            raise ValueError("this id already exist")
        if element.__id > self.__id:
            if self.__left:
                self.__left.add(element)
            else:
                self.__left = element
        else:
            if self.__right:
                self.__right.add(element)
            else:
                self.__right = element

    def get_price(self, id):
        """return price of element with id = argument"""
        if not isinstance(id, int):
            raise TypeError("type of id should be 'int'")
        if id <= 0:
            raise ValueError("id should be >0")
        element = self
        while element and element.__id != id:
            element = element.__left if element.__id < id else element.__right
        if not element:
            raise ValueError("product with this id has not founded")
        return element.__price


Menu = Binary_Tree(5, 15.)
basket = {}
Menu.add(Binary_Tree(1, 100.))
Menu.add(Binary_Tree(2, 30.))
Menu.add(Binary_Tree(3, 20.))
Menu.add(Binary_Tree(4, 25.))
basket[1] = 2
basket[3] = 4
basket[5] = 1
print(sum([basket[x]*Menu.get_price(x) for x in basket.keys()]))
# 2*100+4*20+1*25=200+80+15=295
