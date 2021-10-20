class Binary_Tree:
    """Menu of products"""
    def __init__(self):
        self.__next = 0
        self.__id = 0
        self.__price = 0

    def add(self, price):
        """add product with price = argument into the end of list"""
        if not isinstance(price, float):
            raise TypeError("type of price should be 'float'")
        if price <= 0:
            raise ValueError("price should be >0")
        if not self.__id:
            self.__id = 1
            self.__price = price
        else:
            id = self.__last().__id + 1
            self.__last().__next = Binary_Tree()
            self.__last().__price = price
            self.__last().__id = id

    def __last(self):
        """return last element"""
        last = self
        while last.__next:
            last = last.__next
        return last

    def get_price(self, id):
        """return price of element with id = argument"""
        if not isinstance(id, int):
            raise TypeError("type of id should be 'int'")
        if id <= 0:
            raise ValueError("id should be >0")
        element = self
        while element and element.__id != id:
            element = element.__next
        if not element:
            raise ValueError("product with this id has not founded")
        return element.__price


Menu = Binary_Tree()
basket = {}
Menu.add(15.)
Menu.add(100.)
Menu.add(3.5)
Menu.add(20.)
Menu.add(25.)
basket[1] = 2
basket[3] = 4
basket[5] = 3
print(sum([basket[x]*Menu.get_price(x) for x in basket.keys()]))
# 15*2+3.5*4+25*3=30+14+75=119
