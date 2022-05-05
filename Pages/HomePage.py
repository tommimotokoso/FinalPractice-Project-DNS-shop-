from Pages.BasePage import BasePage
from Pages.ProfilePage import ProfilePage
from Pages.SearchPage import SearchPage
from Config.config import TestData
from Config.locators import Locators
import time


class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Методы связанные с авторизацией пользователя:"""

    def is_signup_link_exist(self):
        if self.is_visible(Locators.BUTTON_SIGNUP):
            return self.is_visible(Locators.BUTTON_SIGNUP)

    def is_users_avatar_exist(self):
        if self.is_visible(Locators.CLICK_PIC):
            return self.is_visible(Locators.CLICK_PIC)

    def is_login_tooltip_exist(self):
        self.do_click(Locators.LOGIN_ASK_ICON)
        if self.is_visible(Locators.LOGIN_AUTH_TOOLTIP):
            return self.is_visible(Locators.LOGIN_AUTH_TOOLTIP)

    def do_logout_from_profile(self):
        self.do_click(Locators.LOGO_LOGOUT)

    def wrong_field(self):
        if self.is_visible(Locators.LOGIN_ERROR_WRONG_FIELD):
            return self.is_visible(Locators.LOGIN_ERROR_WRONG_FIELD)

    def password_open(self, password):
        self.do_send_keys(Locators.FIELD_PASSWORD, password)
        self.do_click(Locators.BUTTON_ICON_HIDE_PASSWORD)
        if self.is_visible(Locators.OPEN_PASSWORD):
            return self.is_visible(Locators.OPEN_PASSWORD)

    def password_hidden(self):
        self.do_click(Locators.BUTTON_ICON_HIDE_PASSWORD)
        if self.is_visible(Locators.HIDDEN_PASSWORD):
            return self.is_visible(Locators.HIDDEN_PASSWORD)

    def recovery_password_success(self, email):
        self.do_click(Locators.FORGOTTEN_PASSWORD)
        self.do_send_keys(Locators.FIELD_EMAIL, email)
        time.sleep(3)
        self.do_click(Locators.BUTTON_RECOVERY_PASSWORD)
        if self.get_text(Locators.BUTTON_CONFIRM_RECOVERY_PASS):
            return self.get_text(Locators.BUTTON_CONFIRM_RECOVERY_PASS)

    def recovery_wrong_field(self, email):
        self.do_click(Locators.FORGOTTEN_PASSWORD)
        self.do_send_keys(Locators.FIELD_EMAIL, email)
        if self.get_text(Locators.FIELD_RECOVERY_ERROR_WRONG):
            return self.get_text(Locators.FIELD_RECOVERY_ERROR_WRONG)

    def do_login(self):
        self.do_click(Locators.BUTTON_SIGNUP)
        self.do_click(Locators.BUTTON_SIGNUP_WITH_PASS)

    def do_login_full(self, email, password):
        self.do_click(Locators.BUTTON_SIGNUP)
        self.do_click(Locators.BUTTON_SIGNUP_WITH_PASS)
        self.do_send_keys(Locators.FIELD_EMAIL, email)
        self.do_send_keys(Locators.FIELD_PASSWORD, password)
        self.do_click(Locators.BUTTON_LOGIN_HOMEPAGE)
        self.do_click(Locators.CLICK_PIC)
        self.do_click(Locators.USER_PROFILE_SETTINGS)
        return ProfilePage(self.driver)

    def do_login_partial(self, email, password):
        self.do_click(Locators.BUTTON_SIGNUP)
        self.do_click(Locators.BUTTON_SIGNUP_WITH_PASS)
        self.do_send_keys(Locators.FIELD_EMAIL, email)
        self.do_send_keys(Locators.FIELD_PASSWORD, password)
        self.do_click(Locators.BUTTON_LOGIN_HOMEPAGE)

    def do_logout(self):
        self.do_click(Locators.CLICK_PIC)
        self.do_click(Locators.USER_PROFILE_SETTINGS)
        self.do_click(Locators.PROFILE_BUTTON_LOGOUT)
        if self.is_visible(Locators.PROFILE_UNAUTHORIZED):
            return self.is_visible(Locators.PROFILE_UNAUTHORIZED)


class SearchFunction(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Методы связанные с поиском товара:"""

    def do_search_text(self, product_name):
        self.do_send_keys(Locators.FIELD_SEARCH, product_name)
        self.do_click(Locators.BUTTON_SEARCH)
        self.get_text(Locators.TITLE_PRODUCT)
        return self.get_text(Locators.TITLE_PRODUCT)

    def do_search_count(self, product_name):
        self.do_send_keys(Locators.FIELD_SEARCH, product_name)
        self.do_click(Locators.BUTTON_SEARCH)
        self.count(Locators.LIST_PRODUCT)
        return self.count(Locators.LIST_PRODUCT)

    def do_search_texts(self, product_name):
        self.do_send_keys(Locators.FIELD_SEARCH, product_name)
        self.do_click(Locators.BUTTON_SEARCH)
        self.get_texts(Locators.LIST_PRODUCT)
        return self.get_texts(Locators.LIST_PRODUCT)

    def do_search_text_incorrect(self, product_name):
        self.do_send_keys(Locators.FIELD_SEARCH, product_name)
        self.do_click(Locators.BUTTON_SEARCH)
        return SearchPage(self.driver)

    def added_to_tves(self):
        self.do_click(Locators.CART_ADD_FIRST_TV)
        self.do_click(Locators.CART_ADD_SECOND_TV)


class CatalogsFunction(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Методы связанные с каталогизацией/сортировкой товара:"""

    def do_catalog_of_tv(self):
        self.do_click(Locators.LINK_TV)
        self.do_click(Locators.LINK_SUB_TV)
        self.do_click(Locators.LINK_SUB_SUB_TV)

    def check_title_tv(self):
        self.get_text(Locators.DESCRIPTION_TV)
        return self.get_text(Locators.DESCRIPTION_TV)

    def filters_on(self):
        self.do_click(Locators.SWITCH_PRICE100)
        self.scroll_to_element(Locators.BUTTON_FILTER_ON)
        self.do_click(Locators.TABS_BAR_DIAGONAL)
        self.do_click(Locators.SWITCH_DIAGONAL55)
        self.do_click(Locators.TABS_SMART_TV)
        self.do_click(Locators.SWITCH_SMART_TV)
        self.do_click(Locators.BUTTON_FILTER_ON)
        self.get_texts(Locators.LIST_FILTERS)
        return self.get_texts(Locators.LIST_FILTERS)

    def auto_filters_on(self, min_price, max_price, min_diagonal, max_diagonal):
        self.do_send_keys(Locators.FIELD_MIN_PRICE, min_price)
        self.do_send_keys(Locators.FIELD_MAX_PRICE, max_price)
        self.scroll_to_element(Locators.BUTTON_FILTER_ON)
        self.do_click(Locators.TABS_BAR_DIAGONAL)
        self.do_send_keys(Locators.FIELD_MIN_DIAGONAL, min_diagonal)
        self.do_send_keys(Locators.FIELD_MAX_DIAGONAL, max_diagonal)
        self.do_click(Locators.BUTTON_FILTER_ON)
        self.get_texts(Locators.LIST_FILTERS)
        return self.get_texts(Locators.LIST_FILTERS)

    def reset_filters(self):
        self.scroll_to_element(Locators.BUTTON_FILTER_ON)
        self.do_click(Locators.BUTTON_FILTER_RESET)
        self.refresh()
        self.count(Locators.LIST_FILTERS)
        return self.count(Locators.LIST_FILTERS)

    def count_filters(self):
        self.scroll_to_element(Locators.BUTTON_FILTER_ON)
        self.do_click(Locators.TABS_BAR_DIAGONAL)
        self.do_click(Locators.SWITCH_DIAGONAL55)
        self.do_click(Locators.TABS_SMART_TV)
        self.do_click(Locators.SWITCH_SMART_TV)
        self.do_click(Locators.BUTTON_FILTER_ON)
        self.count(Locators.LIST_FILTERS)
        return self.count(Locators.LIST_FILTERS)

    def negative_count_filters(self, min_price, max_price):
        self.do_send_keys(Locators.FIELD_MIN_PRICE, min_price)
        self.do_send_keys(Locators.FIELD_MAX_PRICE, max_price)
        self.scroll_to_element(Locators.BUTTON_FILTER_ON)
        self.do_click(Locators.BUTTON_FILTER_ON)
        self.count(Locators.LIST_FILTERS)
        return self.count(Locators.LIST_FILTERS)







