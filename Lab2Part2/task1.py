class Magazine:
    """static class which has list of products as 'Menu' and orders"""
    Menu = []
    orders = []


class Product:
    def __new__(cls, name, price, *args, **kwargs):
        if not isinstance(price, float):
            raise TypeError("type of price should be 'float'")
        if not isinstance(name, str):
            raise TypeError("type of name should be 'str'")
        if price <= 0:
            raise ValueError("price should be >0")
        if not name:
            raise ValueError("name should be written")
        for element in Magazine.Menu:
            if element.name == name:
                raise ValueError("name of product already exist")
        return super(Product, cls).__new__(cls)

    def __init__(self, name, price, description=""):
        if not isinstance(description, str):
            raise TypeError("type of description should be 'str'")
        Magazine.Menu.append(self)
        self.price = price
        self.description = description
        self.name = name


class Costumer:
    """a person who buys products"""
    def __init__(self, surname, name, patronymic, mobile_phone):
        if not isinstance(surname, str):
            raise TypeError("type of surname should be 'str'")
        if not isinstance(name, str):
            raise TypeError("type of name should be 'str'")
        if not isinstance(patronymic, str):
            raise TypeError("type of patronymic should be 'str'")
        if not isinstance(mobile_phone, str):
            raise TypeError("type of mobile_phone should be 'str'")
        if not surname:
            raise ValueError("surname should be written")
        if not surname:
            raise ValueError("surname should be written")
        if not surname:
            raise ValueError("surname should be written")
        if not surname:
            raise ValueError("surname should be written")
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone
        self.money = 0

    def add_money(self, money):
        """give money to costumer, argument 'money' is number"""
        if not isinstance(money, float):
            raise TypeError("type of money should be 'float'")
        if money <= 0:
            raise ValueError("value of money should be more than 0")
        self.money += money


class Order:
    """list of products which want or wanted costumer"""
    def __init__(self, costumer):
        if not isinstance(costumer, Costumer):
            raise TypeError("type of costumer should be 'Costumer'")
        if not costumer:
            raise ValueError("value of costumer should have not value 'null'")
        self.costumer = costumer
        self.__basket = {}
        self.status = 1
        self.id = len(Magazine.orders)
        Magazine.orders.append(self)

    def add(self, product, number):
        """put number of product into basket of order"""
        if self.status != 1:
            return
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

    def total_score(self):
        """return score of all products"""
        value = 0.
        for product in self.__basket:
            value += product.price*self.__basket[product]
        return value

    def pay(self):
        """try pay products in basket of order by costumer`s money"""
        if self.costumer.money >= self.total_score() and self.status == 1:
            self.costumer.money -= self.total_score()
            # costumer gets basket of products
            self.status = 2
            return 1
        return 0

    def undone(self):
        """undone order"""
        if self.status == 1:
            self.status = 0


apple = Product("Apple", 15.)
black_bread = Product("Bread", 14., "black")
salt = Product("Salt", 25.)
Ivan = Costumer("Gus", "Ivan", "Ilych", "095463788")
order = Order(Ivan)
order.add(apple, 10.)
order.add(salt, 1.5)
print(order.total_score())
Ivan.add_money(185.)
if not order.pay():
    print("little money")
    Ivan.add_money(10.)
    order.pay()
    print(order.status)
