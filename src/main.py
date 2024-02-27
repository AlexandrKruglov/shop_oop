from src.category import Category
from src.product import Product
from src.product import Grass, Smartphone
import json
from src.config import PRODUCTS_JSON

if __name__ == '__main__':

    def make_list_products():
        """ получаем список из json файла"""
        with open(PRODUCTS_JSON) as file:
            products_list = json.load(file)
        return products_list


    def make_obj_prod(pr_list):
        """создаем список объектов класса Category
        на вход получаем список из json файла"""
        cat_obj_list = []
        for i in pr_list:
            prod_obj_list = []
            for j in i['products']:
                prod_obj_list.append(Product.create_product(j))
            i['products'] = prod_obj_list
            cat_obj_list.append(Category.create_product(i))
        return cat_obj_list

    class Test_1:

        def __init__(self,name):
            self.name = name

    list_prod_json = make_list_products()
    category_list = make_obj_prod(list_prod_json)
    print(category_list[0])

    for j in Category.get_list_podukts(category_list[0]):
        print(j)

    print(Category.get_obj_from_product(category_list[0], 0) + Category.get_obj_from_product(category_list[1], 0))
    exmp = Grass('gras', 'up', 100.0, 2, 'rus', 3, 'red')
    exemp2 = Smartphone('poco', 'call', 9000, '4', '5', 'm3', 64, 'green')
    exemp3 = Test_1('gfg')

    #print(Category.get_obj_from_product(category_list[0], 0) + exmp)
    #print(exmp)
    print(exemp2)
    print(Category)
    category_list[0].add_obj(exemp2)
    for j in Category.get_list_podukts(category_list[0]):
        print(j)
    print(category_list[0])
    category_list[0].add_obj(exemp3)