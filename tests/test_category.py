import pytest

from src.category import Category, Order, ProdEmptyException
from src.product import Smartphone, Product


@pytest.fixture()
def one_category():
    return Category('test1', 'test1_1', [1, 2])


@pytest.fixture()
def one_smartphon():
    return Smartphone('lg', 'test', 5, 2, '3', 'test', 5, 'red')


@pytest.fixture()
def one_product():
    return Product('lg', 'test', 5, 0)


@pytest.fixture()
def one_order():
    return Order('test', 5, 100)


def test_init_category(one_category):
    assert one_category.name == 'test1'
    assert one_category.description == 'test1_1'
    assert one_category.count_name == 1
    assert one_category.count_products == 2


def test_len_product(one_category):
    assert len(one_category) == 2


def test_get_list_product(one_category):
    assert Category.get_list_podukts(one_category) == [1, 2]


def test_add_obj(one_category, one_smartphon):
    assert Category.add_obj(one_category, one_smartphon) == [1, 2, one_smartphon]
    with pytest.raises(TypeError):
        assert Category.add_obj(one_category, 5) == [1, 2, 5]


def test_add_for_zero_quantity(one_category, one_product):
    assert Category.add_obj(one_category, one_product) == [1, 2]


def test_init_order_zero_quantity(one_order):
    assert Order('test', 0, 100) != type(Order)
    assert isinstance(one_order, Order) is True
