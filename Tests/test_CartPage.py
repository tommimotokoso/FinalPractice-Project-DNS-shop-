import pytest
from Config.config import TestData
from Pages.CartPage import CartPage
from Tests.test_base import BaseTest
from Pages.HomePage import CatalogsFunction
import time


class Test_CartPage(BaseTest):

    """4"""

    def test_cart_is_empty(self):
        self.driver.get(TestData.CART_URL)
        self.CartPage = CartPage(self.driver)
        flag = self.CartPage.is_cart_empty()
        assert flag
        print(""" #45 - Пустая корзина. Проверка по надписи "корзина пуста" """)

    def test_numbers_of_items(self):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        self.Cart = CartPage(self.driver)
        self.Cart.added_to_cart()
        time.sleep(1)
        flag = self.Cart.check_items_to_cart()
        assert flag == "Основные товары (3)"
        self.driver.get(TestData.CART_URL)
        flag2 = self.Cart.check_items_to_cart2()
        assert flag2 == "3 товара"
        print(""" #46 - Добавление трех товаров в корзину. Первая проверка происходит с главной страницы сайта.
        Вторая проверка - со страницы корзины""")

    def test_add_delete_all_items(self):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        self.Cart = CartPage(self.driver)
        self.Cart.added_to_cart2()
        self.driver.get(TestData.CART_URL)
        self.Cart.delete_selected_items()
        flag = self.Cart.is_cart_empty()
        assert flag
        print(""" #47 - Добавление двух товаров в корзину. Удаление из корзины ранее добавленных товаров.
        Проверка на то, что корзина пуста""")

    def test_add_remove_items(self):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        self.Cart = CartPage(self.driver)
        self.Cart.added_to_cart()
        self.driver.get(TestData.CART_URL)
        self.Cart.add_plus_item()
        time.sleep(1)
        self.Cart.add_plus_item()
        time.sleep(1)
        self.Cart.remove_minus_item()
        flag = self.Cart.check_items_to_cart2()
        assert flag == "4 товара"
        print(""" #48 - Добавление трех товаров в корзину. Посредством кнопки "плюс" добавление еще двух товаров (пять).
        Посредством кнопки "минус" уменьшение общего количества товаров до четырех""")


