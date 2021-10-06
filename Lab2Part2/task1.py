class Product:
    def __init__(self, price, description, dimensions):
        if not isinstance(price, float):
            raise TypeError("type of price should be 'float'")
        if not isinstance(description, str):
            raise TypeError("type of description should be 'str'")
        if not isinstance(dimensions, float):
            raise TypeError("type of dimensions should be 'float'")
        if price <= 0:
            raise TypeError("price should be >0")
        if dimensions <= 0:
            raise TypeError("dimensions should be >0")
        if not description:
            raise TypeError("description should be written")
        self.price = price
        self.description = description
        self.dimensions = dimensions


class Costumer:
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
            raise TypeError("surname should be written")
        if not surname:
            raise TypeError("surname should be written")
        if not surname:
            raise TypeError("surname should be written")
        if not surname:
            raise TypeError("surname should be written")
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone


class Order:
    def __init__(self, costumer, products):
        if not isinstance(costumer, Costumer):
            raise TypeError("type of costumer should be 'Costumer'")
        if not isinstance(products, list):
            raise TypeError("products should be the list")
        if not products:
            raise TypeError("products should have 1 element at least")
        for element in products:
            if not isinstance(element, Product):
                raise TypeError(f"type of element {element} of products should be 'Product'")
        self.costumer = costumer
        self.products = list(products)

    def total_value(self):
        value = 0.
        for product in self.products:
            value += product.price
        return value


apple = Product(15., "Fruit", 0.15)
black_bread = Product(7., "Bread", 0.5)
salt = Product(30., "Salt", 1.)
Ivan = Costumer("Gus", "Ivan", "Ilych", "095463788")
order = Order(Ivan, [apple, black_bread, salt])
print(order.total_value())
