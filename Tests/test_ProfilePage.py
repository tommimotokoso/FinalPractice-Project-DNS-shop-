import pytest
from Config.config import TestData
from Pages.HomePage import LoginPage
from Pages.ProfilePage import ProfilePage
from Tests.test_base import BaseTest
import time


class Test_Profile(BaseTest):

    """3"""

    def test_check_closed_profile(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login_partial(TestData.LOGIN_VALID_EMAIL, TestData.LOGIN_VALID_PASSWORD)
        self.ProfilePage = ProfilePage(self.driver)
        self.ProfilePage.get(TestData.PROFILE_URL)
        flag = self.ProfilePage.do_closed_profile()
        assert flag
        time.sleep(1)
        self.LoginPage.do_logout_from_profile()
        print(""" #42 - Открытый профиль делается закрытым.
        Проверка по активной кнопке "открыть профиль" (после закрытия)""")

    def test_check_open_profile(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login_partial(TestData.LOGIN_VALID_EMAIL, TestData.LOGIN_VALID_PASSWORD)
        self.ProfilePage = ProfilePage(self.driver)
        self.ProfilePage.get(TestData.PROFILE_URL)
        flag = self.ProfilePage.do_opened_profile()
        assert flag
        time.sleep(1)
        self.LoginPage.do_logout_from_profile()
        print(""" #43 - Закрытый профиль делается открытым.
        Проверка по активной кнопке "закрыть профиль" (после открытия)""")

    @pytest.mark.xfail(reason="После обновления страницы, статус сбрасывается")
    def test_change_profile_status(self):
        """БАГ"""
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login_partial(TestData.LOGIN_VALID_EMAIL, TestData.LOGIN_VALID_PASSWORD)
        self.ProfilePage = ProfilePage(self.driver)
        self.ProfilePage.get(TestData.PROFILE_URL)
        flag = self.ProfilePage.do_change_status(TestData.PROFILE_STATUS_CHANGE)
        print(flag)
        assert flag == TestData.PROFILE_STATUS_CHANGE
        print(""" #44 - Попытка смены статуса в профиле. После обновления страницы статус не сохраняется""")






