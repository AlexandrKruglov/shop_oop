class Category:
    """класс категория хранит название категории,
      описание категории,
      список входящих продуктов"""
    name: str
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
        self.__products.append(obj_prod)
        return self.__products

    @property
    def input_info(self):
        list_product = self.__products
        new_list = []
        for i in list_product:
            new_list.append(str(i))
        return "\n".join(new_list)

