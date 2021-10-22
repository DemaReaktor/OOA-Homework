class Product:
    """product"""
    __menu = []

    def __new__(cls, name, price, description=''):
        for element in Product.__menu:
            if element.name == name:
                raise ValueError("name of product already exist")
        return super(Product, cls).__new__(cls)

    def __init__(self, name, price, description=""):
        Product.__menu.append(self)
        self.__price = price
        self.__description = description
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("type of price should be 'float'")
        if value <= 0:
            raise ValueError("price should be >0")
        self.__price = value

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("type of description should be 'str'")
        self.__description = value

    @classmethod
    def get_menu(cls):
        """return a list of all products"""
        return cls.__menu


class Costumer:
    """a person who buys products"""
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__mobile_phone = mobile_phone
        self.__money = 0

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("type of surname should be 'str'")
        if not value:
            raise ValueError("surname should be written")
        self.__surname = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("type of name should be 'str'")
        if not value:
            raise ValueError("name should be written")
        self.__name = value

    @patronymic.setter
    def patronymic(self, value):
        if not isinstance(value, str):
            raise TypeError("type of patronymic should be 'str'")
        if not value:
            raise ValueError("patronymic should be written")
        self.__patronymic = value

    @mobile_phone.setter
    def mobile_phone(self, value):
        if not isinstance(value, str):
            raise TypeError("type of mobile_phone should be 'str'")
        if not value:
            raise ValueError("name mobile_phone be written")
        self.__mobile_phone = value

    def add_money(self, money):
        """give money to costumer, argument 'money' is number"""
        if not isinstance(money, float):
            raise TypeError("type of money should be 'float'")
        if money <= 0:
            raise ValueError("value of money should be more than 0")
        self.__money += money

    def get_money(self, money):
        """costumer try to give money, argument is a number"""
        if not isinstance(money, float):
            raise TypeError("type of money should be 'float'")
        if money <= 0:
            raise ValueError("value of money should be more than 0")
        if money > self.__money:
            raise ValueError("costumer does not have enough money")
        self.__money -= money


class Order:
    """list of products which want or wanted costumer"""
    orders = []

    def __init__(self, costumer):
        if not isinstance(costumer, Costumer):
            raise TypeError("type of costumer should be 'Costumer'")
        if not costumer:
            raise ValueError("value of costumer should have not value 'null'")
        self.__costumer = costumer
        self.__basket = {}
        self.__status = 1
        self.__id = len(Order.orders)
        Order.orders.append(self)

    @property
    def costumer(self):
        return self.__costumer

    @property
    def status(self):
        if self.__status == 2:
            return 'done'
        if self.__status:
            return 'active'
        return 'undone'

    @property
    def basket(self):
        return self.__basket

    @property
    def id(self):
        return self.__id

    def add_product(self, product, number):
        """put number of product into basket of order"""
        if self.__status != 1:
            raise ValueError('order already is not active')
        if not isinstance(product, Product):
            raise TypeError("type of product should be 'Product'")
        if not isinstance(number, float):
            raise TypeError("type of number should be 'float'")
        if not product:
            raise ValueError("product should have not value 'null'")
        if number <= 0:
            raise ValueError("number should be more than 0")
        if self.__basket.get(product):
            self.__basket[product] += number
        else:
            self.__basket[product] = number

    def remove_product(self, product, number):
        """number of this product is trying to be removed from order"""
        if self.__status != 1:
            raise ValueError('order already is not active')
        if not isinstance(product, Product):
            raise TypeError("type of product should be 'Product'")
        if not isinstance(number, float):
            raise TypeError("type of number should be 'float'")
        if not product:
            raise ValueError("product should have not value 'null'")
        if number <= 0:
            raise ValueError("number should be more than 0")
        if self.__basket.get(product):
            if number < self.__basket[product]:
                self.__basket[product] -= number
            elif number == self.__basket[product]:
                self.__basket.pop(product)
            else:
                raise ValueError('order have number of product less than argument')
        else:
            raise ValueError('there is not this product in order')

    def total_score(self):
        """return score of all products"""
        value = 0.
        for product in self.__basket:
            value += product.price*self.__basket[product]
        return value

    def pay(self):
        """try pay products in basket of order by costumer`s money"""
        if self.__status == 1:
            self.__costumer.get_money(self.total_score())
            # costumer gets basket of products
            self.__status = 2
        else:
            raise ValueError('order already is not active')

    def undone(self):
        """undone order"""
        if self.__status == 1:
            self.__status = 0
        else:
            raise ValueError('order already is not active')


apple = Product("Apple", 15.)
black_bread = Product("Bread", 14., "black")
salt = Product("Salt", 25.)
Ivan = Costumer("Gus", "Ivan", "Ilych", "095463788")
order = Order(Ivan)
order.add_product(apple, 10.)
order.add_product(salt, 1.5)
print(order.total_score())
Ivan.add_money(185.)
try:
    order.pay()
except Exception as exeption:
    print('error:', exeption.args[0])
    Ivan.add_money(10.)
    order.pay()
    print('status:', order.status)
