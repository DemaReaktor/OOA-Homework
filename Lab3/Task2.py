import os.path
import datetime
import json


class Ingredients:
    __ingredients = {}

    @classmethod
    def create_ingredient(cls, name, price):
        if not isinstance(name, str):
            raise TypeError('name should be type "str"')
        if not name:
            raise ValueError('name should be not null')
        if not isinstance(price, float):
            raise TypeError('price should be type "float"')
        if price <= 0:
            raise ValueError('price should be more 0')
        for element in cls.__ingredients.keys():
            if element == name:
                raise AttributeError('ingredient with this name already exists')
        cls.__ingredients[name] = price

    @classmethod
    def ingredients(cls):
        return cls.__ingredients


class Pizza:
    __price_of_cooking = 10.
    __pizzas = []

    def __init__(self, name, size=1.):
        if not isinstance(name, str):
            raise TypeError('name should be type "str"')
        if not name:
            raise ValueError('name value should be not null')
        if name != 'costume' and name in [element.name for element in Pizza.__pizzas]:
            raise AttributeError('pizza with this name already exists')
        self.__name = name
        self.__ingredients = set()
        self.__ingredients.add('bread')
        self.size = size

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def ingredients(self):
        return self.__ingredients

    @size.setter
    def size(self, value):
        if not isinstance(value, float):
            raise TypeError('size should be class "float"')
        if value <= 0:
            raise ValueError('size value should be more 0')
        self.__size = value

    def add_ingredient(self, ingredient):
        if not isinstance(ingredient, str):
            raise TypeError('ingredient should be class "str"')
        if not ingredient:
            raise ValueError('ingredient should have not null')
        self.__ingredients.add(ingredient)

    def add_ingredient_by_costumer(self, ingredient):
        if not isinstance(ingredient, str):
            raise TypeError('ingredient should be class "str"')
        if not ingredient:
            raise ValueError('ingredient should have not null')
        self.__ingredients.add(ingredient)
        self.__name = 'costume'

    @property
    def price(self):
        summa = 0.
        for element in self.__ingredients:
            summa += Ingredients.ingredients()[element]
        return summa*self.__size*self.__size+self.__price_of_cooking

    def is_pizza_of_day(self, day_of_week):
        return False

    @classmethod
    def add_pizza_to_menu(cls, pizza):
        if not issubclass(type(pizza), Pizza):
            raise TypeError('pizza should be type pizza or be son of this type')
        cls.__pizzas.append(pizza)

    @classmethod
    def menu(cls):
        return cls.__pizzas

    def __str__(self):
        ingredients = ''
        for element in self.__ingredients:
            ingredients += element+', '
        return self.name+': size='+str(self.size)+', ingredients='+ingredients+'price='+str(self.price)+'\n'

    @classmethod
    def get_pizza(cls, name):
        return cls.copy(cls.__pizzas[name]) if name in cls.__pizzas else 'pizza was not found'

    @classmethod
    def copy(cls, pizza):
        return type(pizza)(pizza.name, pizza.size)


class MondayPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)

    def is_pizza_of_day(self, day_of_week):
        return day_of_week == 1


class TuesdayPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)

    def is_pizza_of_day(self, day_of_week):
        return day_of_week == 2


class WednesdayPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)

    def is_pizza_of_day(self, day_of_week):
        return day_of_week == 3


class ThursdayPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)

    def is_pizza_of_day(self, day_of_week):
        return day_of_week == 4


class FridayPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)

    def is_pizza_of_day(self, day_of_week):
        return day_of_week == 5


class SaturdayPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)

    def is_pizza_of_day(self, day_of_week):
        return day_of_week == 6


class SundayPizza(Pizza):
    def __init__(self, name, size):
        super().__init__(name, size)

    def is_pizza_of_day(self, day_of_week):
        return day_of_week == 7


def read_file(file_name):
    with open(file_name, 'r') as file:
        pizzas = json.load(file)
        for element in pizzas:
            list_properties = list(element.keys())
            type_pizza = eval(list_properties[0].split('_')[1])
            name_pizza = element[list_properties[0]]
            ingredients_pizza = []
            for ingredient in element[list_properties[1]]:
                ingredients_pizza.append(ingredient)
            size = element[list_properties[2]]
            pizza_new = type_pizza(name_pizza, float(size))
            Pizza.add_pizza_to_menu(pizza_new)
            for ingredient in ingredients_pizza:
                pizza_new.add_ingredient(ingredient)
    with open('ingredients.json', 'r') as file:
        ingredients = json.load(file)
        for element in ingredients.keys():
            Ingredients.create_ingredient(element, float(ingredients[element]))


file_path = 'pizza.json'
if os.path.isfile(file_path):
    read_file(file_path)
is_admin = False
pizza = None
sentence = 'commands: {show menu},{buy pizza},{exit},{get pizza: <name>},{add ingredient: <name>}'
print(sentence + ',set size: <size>,{show ingredients}, {show pizzas of day}')
while True:
    command = input()
    if command == 'show menu':
        for element in Pizza.menu():
            print(element)
    elif command == 'admin':
        is_admin = True
        print('+ {add ingredient: <name> <price>},{add pizza: <name> <week>}')
    elif command == 'exit':
        exit()
    elif command == 'show pizzas of day':
        print('pizzas of days:\n')
        for element in Pizza.menu():
            if element.is_pizza_of_day(datetime.date.today().weekday()+1):
                print(element)
    elif command == 'show ingredients':
        print(Ingredients.ingredients())
    elif not command.find('get pizza: '):
        if command.replace('get pizza: ', ''):
            pizza = Pizza.get_pizza(command.replace('get pizza: ', ''))
        if isinstance(pizza, str):
            print(pizza)
            pizza = None
        else:
            print('+')
    elif pizza:
        if command == 'buy pizza':
            pizza = None
            print('+')
        elif not command.find('set size: ') and command.replace('set size: ', '').isdigit():
            pizza.size = int(command.replace('set size: ', ''))
            print(pizza.price)
        elif not command.find('add ingredient: ') and command.replace('add ingredient: ', '').isdigit():
            pizza.add_ingredient_by_costumer(command.replace('add ingredient: ', ''))
            print(pizza.price)
    else:
        print('unknown command')
