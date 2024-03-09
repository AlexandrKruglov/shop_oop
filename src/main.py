from src.category import Category, Order, ProdEmptyException
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


    list_prod_json = make_list_products()  # список из products.json
    category_list = make_obj_prod(list_prod_json)  # список категорий

    # for j in Category.get_list_podukts(category_list[0]):
    #     print(j)
    # print(Category.get_obj_from_product(category_list[0], 0) + Category.get_obj_from_product(category_list[1], 0))

    exmp = Grass('gras', 'up', 100.0, 2, 'rus', 3, 'red')
    exemp2 = Smartphone('poco', 'call', 9000, 0, '5', 'm3', 64, 'green')
    exemp3 = Category('car', 'drive', [])

    # print(Category.sub_prod(category_list, ex_order))
    print(category_list[0])

    category_list[0].add_obj(exemp2)  # добавляем продукт в список продуктов данной категории
    print(category_list[0])

    x_order = Order('Iphone 15', 0, 100)  # создаем экземпляр класса заказ

    print(category_list[0].get_average_price())  # высчитываем средний ценик товаров данной категории
    print(exemp3.get_average_price())  # если в категории нет товаров возвращает ноль

