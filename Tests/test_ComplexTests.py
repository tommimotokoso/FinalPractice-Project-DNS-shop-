import time

import pytest
from Config.config import TestData
from Pages.HomePage import LoginPage
from Pages.HomePage import SearchFunction
from Pages.HomePage import CatalogsFunction
from Tests.test_base import BaseTest
from Pages.CartPage import CartPage
from Pages.ProfilePage import ProfilePage


class Test_Complex(BaseTest):

    """2"""

    def test_smoke_test_DNS(self):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        self.Cart = CartPage(self.driver)
        self.Cart.added_to_cart2()
        self.driver.get(TestData.CART_URL)
        flag = self.Cart.go_to_checkout()
        time.sleep(3)
        print(flag)
        assert flag
        print(""" #49 - дымовое тестирование - самый короткий путь до кнопки "оформление заказа".
        Проверка происходит по наличию этой кнопки на странице""")

    def test_complex_test_DNS(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login_partial(TestData.LOGIN_VALID_EMAIL, TestData.LOGIN_VALID_PASSWORD)
        flag = self.LoginPage.is_users_avatar_exist()
        assert flag
        self.ProfilePage = ProfilePage(self.driver)
        flag2 = self.ProfilePage.is_logout_link_exist()
        assert flag2
        self.SearchFunction = SearchFunction(self.driver)
        self.SearchFunction.do_search_text(TestData.SEARCH_TV)
        self.SearchFunction.added_to_tves()
        self.driver.get(TestData.CART_URL)
        self.Cart = CartPage(self.driver)
        flag3 = self.Cart.check_items_to_cart2()
        assert flag3 == "2 товара"
        self.Cart = CartPage(self.driver)
        self.Cart.delete_selected_items()
        flag4 = self.Cart.is_cart_empty()
        assert flag4
        self.LoginPage = LoginPage(self.driver)
        flag5 = self.LoginPage.do_logout()
        assert flag5
        print(""" #50 - Комплексное тестирование некоторого функционала сайта.
        Сначало проверка авторизации пользователя - проверка (flag)  по наличию кнопки с аватаром пользователя.
        Далее производится вход на страницу профиля пользвателя - проверка (flag2) по наличию кнопки разлогина.
        В поле поиска вводится название товара (негативное тестирование); система должна распознать запрос
        и добавить два телевизора в корзину - проверка (flag3) по надписи со страницы корзины.
        Далее - удаление ранее добавленного товара из корзины - проверка (flag4), что корзина пуста.
        Заключительная часть - разлогин пользователя. Проверка (flag5) по наличию кнопки "войти в профиль" """)


