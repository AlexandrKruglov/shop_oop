from src.product import Product, MixinLog
from abc import ABC, abstractmethod


class TradeTurnover(ABC):
    name: str

    @abstractmethod
    def __init__(self, ):
        pass

    def __str__(self):
        pass

    def init_zero(self, quantity):
        """метод проверяет количество товара если 0 выдает ошибку
        использую в добавление продукта в список продуктов категории и  создании екземпляра класса заказ"""
        if quantity <= 0:
            raise ProdEmptyException()
        else:
            self.quantity = quantity
            return self.quantity


class Category(MixinLog, TradeTurnover):
    """класс категория хранит название категории,
      описание категории,
      список входящих продуктов"""
    description: str
    products: list
    count_name = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.count_name += 1
        self.count_products = len(self.__products)
        super().__init__()

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.name}, Количество товаров: {len(self)}'

    @classmethod
    def create_product(cls, dict_prod):
        """создает объект класса продукт из словаря
        :param dict_prod: словарь
        :return: объект клааса продукт"""
        new_obj_prod = cls(dict_prod["name"], dict_prod["description"], dict_prod["products"])
        return new_obj_prod

    def get_list_podukts(self):
        """возвращает список продуктов"""
        return self.__products

    def get_obj_from_product(self, num):
        return self.__products[num]

    def add_obj(self, obj_prod):
        """ добавляет продукт в список продуктов принимет объект класса продукт"""
        if isinstance(obj_prod, Product):
            try:
                self.init_zero(obj_prod.quantity)
            except ProdEmptyException as e:
                print(e)
            else:
                self.__products.append(obj_prod)
                print("товар добавлен")
                return self.__products
            finally:
                print("обработка завершина")
                return self.__products
        raise "добавляемый обект не является классом Product или его наследником"

    def get_average_price(self):
        """подсчитывает средний ценник всех товаров .
         При отсутствии товаров возвращает ноль"""
        total_price = 0
        for i in self.__products:
            total_price += i.price
        try:
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0

    @classmethod
    def sub_prod(cls, list_cls, obj_prod):
        """ удаляет кол-во товара по заказу из списк продуктов """
        for j in list_cls:
            for i in j.__products:
                if i.name == obj_prod.name:
                    temp = i.quantity - obj_prod.quantity
                    if temp < 0 :
                        raise "такого количества нет"
                    i.quantity = temp
                    return i.__str__
        raise "нет этого товара"

    @property
    def input_info(self):
        """выводит список продуктов в нужном формате"""
        list_product = self.__products
        new_list = []
        for i in list_product:
            new_list.append(str(i))
        return "\n".join(new_list)


class Order(MixinLog, TradeTurnover):
    """класс заказ """
    quantity: int
    price: float

    def __init__(self, name, quantity, price):

        try:
            self.name = name
            self.price = price
            self.quantity = self.init_zero(quantity)
            super().__init__()
        except ProdEmptyException as e:
            print(e)
        else:
            print("заказ добавлен")
        finally:
            print("обработка заказа завершина")

    def __str__(self):
        return f'заказ {self.name}, кол-во {self.quantity}, на сумму {self.price * self.quantity}'


class ProdEmptyException(Exception):

    def __init__(self, *args, **kwargs):
            self.masege = args[0] if args else 'ошибка количество товара равно нулю'

    def __str__(self):
        return self.masege
