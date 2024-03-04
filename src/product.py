from abc import ABC, abstractmethod


class ProdAbs(ABC):
    @abstractmethod
    def __init__(self):
        pass


class MixinLog:
    ID = 1

    def __init__(self):
        self.id = self.ID
        MixinLog.ID +=1
        super().__init__()
        print(self.__repr__())

    def __repr__(self):
        return f'создан {self.__class__} , id {self.id}, {self.__str__()} '


class Product(MixinLog, ProdAbs):
    """
    класс продукт хранит название продукта,
    описание продукта
    стоимость продукта
    количество продукта
    """
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()
    def __str__(self):
        return f'{self.name}, {self.price}руб. Остаток: {self.quantity}шт.'

    @classmethod
    def create_product(cls, dict_prod):
        """создает объект класса продукт из словаря
        :param dict_prod: словарь
        :return: объект клааса продукт"""
        new_obj_prod = cls(dict_prod["name"], dict_prod["description"], dict_prod["price"], dict_prod["quantity"])
        return new_obj_prod

    @property
    def chek_price(self):
        """возвращает цену продукта"""
        return self.price

    @chek_price.setter
    def chek_price(self, new_price):
        """изменяет цену продукта
        :param new_price: новая цена
        :return: если новая цена = 0 или < 0 возвращает "некоректная цена"
        в противном случае меняет цену"""
        if new_price <= 0:
            print("некоректная цена")
        self.price = new_price

    def __add__(self, other):
        """складывает общуюсумму стоимость всех единиц двух видов продукта"""
        if type(other) == type(self):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class RangeProductc:
    """который  дает возможность использовать цикл for
    для прохода по всем товарам данной категории.
    при запросе
    for i in RangeProductc(len(Сategory)):
    print(i)"""

    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.value = -1
        return self

    def __next__(self):
        if self.value + 1 < self.stop:
            self.value += 1
            return self.value
        else:
            raise StopIteration


class Smartphone(Product):
    """класс смартфотны наследуется от класса продукт """
    performance: str
    model: str
    memory: int

    def __init__(self, name, description, price,
                 quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class Grass(Product):
    """класс трава газонная наследуется от класса продукт"""
    made_in: str
    growing_period: int

    def __init__(self, name, description, price,
                 quantity, made_in,growing_period, color):
        super().__init__(name, description, price, quantity)
        self.made_in = made_in
        self.growing_period = growing_period
        self.color = color
