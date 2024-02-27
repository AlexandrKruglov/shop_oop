import pytest

from src.category import Category


@pytest.fixture()
def one_category():
    return Category('test1', 'test1_1', [1, 2])


def test_init_category(one_category):
    assert one_category.name == 'test1'
    assert one_category.description == 'test1_1'
    assert one_category.count_name == 1
    assert one_category.count_products == 2


def test_len_product(one_category):
    assert len(one_category) == 2


def test_get_list_product(one_category):
    assert Category.get_list_podukts(one_category) == [1, 2]


def test_add_obj(one_category):
    assert Category.add_obj(one_category, 3) == [1, 2, 3]

