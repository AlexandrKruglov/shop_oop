from src.category import Category
from src.product import Product
from src.product import Grass
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


    list_prod_json = make_list_products()
    category_list = make_obj_prod(list_prod_json)
    print(category_list[0])

    for j in Category.get_list_podukts(category_list[0]):
        print(j)

    print(Category.get_obj_from_product(category_list[0], 0) + Category.get_obj_from_product(category_list[1], 0))
    exmp = Grass('gras', 'up', 100.0, 2, 'rus', 3, 'red')
    print(Category.get_obj_from_product(category_list[0], 0) + exmp)