import pytest
from Config.config import TestData
from Pages.HomePage import LoginPage
from Pages.HomePage import SearchFunction
from Pages.HomePage import CatalogsFunction
from Tests.test_base import BaseTest
import time


class Test_login(BaseTest):

    """10"""

    def test_signup_link_visible(self):
        self.LoginPage = LoginPage(self.driver)
        flag = self.LoginPage.is_signup_link_exist()
        assert flag
        print(""" #1 - проверка на видимость кнопки "Войти", то есть пользователь незалогинен""")

    def test_Login_valid(self):
        self.LoginPage = LoginPage(self.driver)
        ProfilePage = self.LoginPage.do_login_full(TestData.LOGIN_VALID_EMAIL, TestData.LOGIN_VALID_PASSWORD)
        title = ProfilePage.get_profile_page_title(TestData.PROFILE_TITLE)
        assert title == TestData.PROFILE_TITLE
        time.sleep(1)
        self.LoginPage.do_logout_from_profile()
        print(""" #2 - авторизация пользователя. Проверка осуществляется по заголовку страницы""")

    def test_login_novalid_empty_email(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login_partial(TestData.LOGIN_EMPTY_EMAIL, TestData.LOGIN_VALID_PASSWORD)
        flag = self.LoginPage.wrong_field()
        assert flag
        print(""" #3 - при отсутствии символов в поле "email" появляется сообщение об ошибке """)

    def test_login_novalid_empty_password(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login_partial(TestData.LOGIN_VALID_EMAIL, TestData.LOGIN_EMPTY_PASSWORD)
        flag = self.LoginPage.wrong_field()
        assert flag
        print(""" #4 - при отсутствии символов в поле "Пароль" появляется сообщение об ошибке """)

    def test_login_novalid_email(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login_partial(TestData.LOGIN_NO_VALID_EMAIL, TestData.LOGIN_VALID_PASSWORD)
        flag = self.LoginPage.wrong_field()
        assert flag
        print(""" #5 - при неверном вводе почты в поле "email" появляется сообщение об ошибке """)

    def test_login_novalid_password(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login_partial(TestData.LOGIN_VALID_EMAIL, TestData.LOGIN_NO_VALID_PASSWORD)
        flag = self.LoginPage.wrong_field()
        assert flag
        print(""" #6 - при неверном вводе пароля в поле "Пароль" появляется сообщение об ошибке """)

    def test_login_tooltip_exist(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login()
        flag = self.LoginPage.is_login_tooltip_exist()
        assert flag
        print(""" #7 - при нажатии на значок вопроса появляется контекстное меню с подсказкой для авторизации""")

    def test_login_open_password(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login()
        flag1 = self.LoginPage.password_open(TestData.LOGIN_VALID_PASSWORD)
        assert flag1
        flag2 = self.LoginPage.password_hidden()
        assert flag2
        print(""" #8 - при первом нажатии на значок скрытия пароля, иконка изменяется (пароль скрыт);
        при повторном нажатии, иконка меняется еще раз (пароль виден)""")

    def test_recovery_password_success(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login()
        flag = self.LoginPage.recovery_password_success(TestData.LOGIN_VALID_EMAIL)
        assert flag == "Подтвердить"
        print(""" #9 - процедура восстановления пароля исправна - видна кнопка "подтвердить" запрос смс на телефон""")

    def test_recovery_wrong_field(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login()
        flag = self.LoginPage.recovery_wrong_field(TestData.LOGIN_NO_VALID_EMAIL)
        assert flag == "Введите корректный логин (e-mail или телефон)"
        print(""" #10 - неверная почта при процедуре восстановления пароля выдает соответсвующую ошибку""")


class Test_Search(BaseTest):

    """12"""

    def test_search_correct(self):
        self.SearchFunction = SearchFunction(self.driver)
        flag = self.SearchFunction.do_search_text(TestData.SEARCH_FULL_LOWER)
        assert flag == "Смартфоны"
        print(""" #11 - после ввода "смартфон" в поисковом поле, появляется страница с каталогом смартфонов.
        Проверка осуществляется по слову заголовка "смартфоны" """)

    def test_search_count_correct(self):
        self.SearchFunction = SearchFunction(self.driver)
        flag = self.SearchFunction.do_search_count(TestData.SEARCH_FULL_LOWER)
        assert flag > 3
        print(""" #12 - после ввода "смартфон" в поисковом поле, появляется страница с каталогом смартфонов.
        Проверка осуществляется по количеству найденного товара""")

    def test_search_list_correct(self):
        self.SearchFunction = SearchFunction(self.driver)
        flag = self.SearchFunction.do_search_texts(TestData.SEARCH_FULL_LOWER)
        for title in flag:
            assert "Смартфон" in title
        print(""" #13 - после ввода "смартфон" в поисковом поле, появляется страница с каталогом смартфонов.
        Проверка осуществляется по первому товару в появившемся списке""")

    @pytest.mark.parametrize("search", [TestData.SEARCH_FULL_LOWER, TestData.SEARCH_REVERSE_NAME,
                                        TestData.SEARCH_FULL_BIGGER, TestData.SEARCH_PARTIAL_NAME,
                                        TestData.SEARCH_UNDER_SCORE_NAME, TestData.SEARCH_TRIPLE_N,
                                        TestData.SEARCH_SHUFFLE_LETTERS],
                             ids=["смартфон", "cvfhnajy", "СМАРТФОН", "смар",
                                  "_____смартфон", "смартфоннн", "срамтфон"])
    def test_full_search_list_correct(self, search):
        self.SearchFunction = SearchFunction(self.driver)
        flag = self.SearchFunction.do_search_texts(search)
        for title in flag:
            assert "Смартфон" in title
        print(""" #14-20 - различные вариации слова "смартфон" система должна распознать запрос пользователя.
        Проверка осуществляется по первому товару в появившемся списке""")

    def test_search_incorrect(self):
        self.SearchFunction = SearchFunction(self.driver)
        SearchPage = self.SearchFunction.do_search_text_incorrect(TestData.SEARCH_NO_VALID)
        title = SearchPage.get_search_page_title(TestData.SEARCH_TITLE)
        assert title == TestData.SEARCH_TITLE
        print(""" #21 - некорректный поисковый запрос пользователя ведет на заранее заготовленную страницу""")

class Test_Catalogs(BaseTest):

    """20"""

    def test_catalog_tv(self):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        flag = self.Catalogs.check_title_tv()
        time.sleep(5)
        assert flag == "Телевизоры"
        print(""" #22 - выбор товара "телевизор" через каталог. Проверка осуществляется по слову "Телевизоры" """)

    def test_filters_tv(self):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        flag = self.Catalogs.filters_on()
        if TestData.FILTERS_TOTAL_DIAG_55x65 and TestData.FILTERS_TOTAL_PRICE_more_100k \
                and TestData.FILTERS_TOTAL_SMART_TV_ON in flag:
            elem = 1
        else:
            elem = 0
        assert elem == 1
        print(""" #23 - проверка работы фильтров (диагональ, цена, смарт_тв. Тест успешные если все три фильтра
        присутствуют в шапке фильтров""")

    @pytest.mark.parametrize("min_price", [TestData.FILTERS_MIN_PRICE1, TestData.FILTERS_MIN_PRICE2], ids=["9000p", "100000p"])
    @pytest.mark.parametrize("max_price", [TestData.FILTERS_MAX_PRICE1, TestData.FILTERS_MAX_PRICE2], ids=["30000p", "6000000p"])
    @pytest.mark.parametrize("min_diagonal", [TestData.FILTERS_MIN_DIAGONAL1, TestData.FILTERS_MIN_DIAGONAL2], ids=["23", "60"])
    @pytest.mark.parametrize("max_diagonal", [TestData.FILTERS_MAX_DIAGONAL1, TestData.FILTERS_MAX_DIAGONAL2], ids=["50", "84"])
    def test_auto_filters_tv(self, min_price, max_price, min_diagonal, max_diagonal):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        flag = self.Catalogs.auto_filters_on(min_price, max_price, min_diagonal, max_diagonal)
        if TestData.FILTERS_TOTAL_DIAG_23x50 and TestData.FILTERS_TOTAL_PRICE_9kx30k \
                or TestData.FILTERS_TOTAL_DIAG_23x50 and TestData.FILTERS_TOTAL_PRICE_100kx6000k \
                or TestData.FILTERS_TOTAL_DIAG_23x50 and TestData.FILTERS_TOTAL_PRICE_100kx30k \
                or TestData.FILTERS_TOTAL_DIAG_23x50 and TestData.FILTERS_TOTAL_PRICE_9kx6000k \
                or TestData.FILTERS_TOTAL_DIAG_23x84 and TestData.FILTERS_TOTAL_PRICE_9kx30k \
                or TestData.FILTERS_TOTAL_DIAG_23x84 and TestData.FILTERS_TOTAL_PRICE_9kx6000k \
                or TestData.FILTERS_TOTAL_DIAG_23x84 and TestData.FILTERS_TOTAL_PRICE_100kx30k \
                or TestData.FILTERS_TOTAL_DIAG_23x84 and TestData.FILTERS_TOTAL_PRICE_100kx6000k \
                or TestData.FILTERS_TOTAL_DIAG_60x50 and TestData.FILTERS_TOTAL_PRICE_9kx30k \
                or TestData.FILTERS_TOTAL_DIAG_60x50 and TestData.FILTERS_TOTAL_PRICE_9kx6000k \
                or TestData.FILTERS_TOTAL_DIAG_60x50 and TestData.FILTERS_TOTAL_PRICE_100kx30k \
                or TestData.FILTERS_TOTAL_DIAG_60x50 and TestData.FILTERS_TOTAL_PRICE_100kx6000k \
                or TestData.FILTERS_TOTAL_DIAG_60x84 and TestData.FILTERS_TOTAL_PRICE_9kx30k \
                or TestData.FILTERS_TOTAL_DIAG_60x84 and TestData.FILTERS_TOTAL_PRICE_9kx6000k \
                or TestData.FILTERS_TOTAL_DIAG_60x84 and TestData.FILTERS_TOTAL_PRICE_100kx30k \
                or TestData.FILTERS_TOTAL_DIAG_60x84 and TestData.FILTERS_TOTAL_PRICE_100kx6000k in flag:
            elem = 1
        else:
            elem = 0
        assert elem == 1
        print(""" #24-39 - Проверка параметризации тестирования фильтров. Помимо стандартных сценариев,
        система должна корректно обработать негативные (цена от 100000р до 30000р, диагональ от 60 до 50)""")

    def test_filters_reset(self):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        flag = self.Catalogs.count_filters()
        assert flag / 2 == 2
        flag2 = self.Catalogs.reset_filters()
        assert flag2 == 0
        print(""" #40 - Проверка сброса фильтров. Сначало запрашивается товар с двумя фильтрами.
        Проверка идет по наличию шапок фильтров. Результат делится на два,
        так как с самим названием фильтра идет и иконка отмены фильтра.
        Затем следует сброс всех кнопкой с помощью соответсвующей кнопки и снова идет проверка шапки фильтров (0)""")

    def test_negative_price(self):
        self.Catalogs = CatalogsFunction(self.driver)
        self.Catalogs.do_catalog_of_tv()
        flag = self.Catalogs.negative_count_filters(TestData.FILTERS_NEGATIVE_PRICE1, TestData.FILTERS_NEGATIVE_PRICE2)
        print(flag)
        assert flag == 0
        print(""" #41 - Попытка в фильтр цены вбить негативные (нарушающие работу фильтра) значения.
        В шапке фильтров не должно появиться элементов""")
