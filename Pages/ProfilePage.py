from Pages.BasePage import BasePage
from Config.config import TestData
from Config.locators import Locators

class ProfilePage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.PROFILE_URL)

    """Методы связанные с профайлом пользователя:"""

    def get_profile_page_title(self, title):
        return self.get_title(title)

    def is_logout_link_exist(self):
        if self.is_visible(Locators.PROFILE_BUTTON_LOGOUT):
            return self.is_visible(Locators.PROFILE_BUTTON_LOGOUT)

    def get(self, url):
        self.driver.get(TestData.PROFILE_URL)

    def refresh(self):
        self.driver.refresh()

    def do_closed_profile(self):
        self.do_click(Locators.BUTTON_OPEN_PROFILE)
        if self.is_visible(Locators.BUTTON_CLOSED_PROFILE):
            return self.is_visible(Locators.BUTTON_CLOSED_PROFILE)

    def do_opened_profile(self):
        self.do_click(Locators.BUTTON_CLOSED_PROFILE)
        if self.is_visible(Locators.BUTTON_OPEN_PROFILE):
            return self.is_visible(Locators.BUTTON_OPEN_PROFILE)

    def do_change_status(self, status):
        self.do_click(Locators.INFO_STATUS_CHANGE)
        self.do_send_keys(Locators.FIELD_INFO_STATUS, status)
        self.do_click(Locators.BUTTON_SAVE_INFO_STATUS)
        self.refresh()
        if self.get_text(Locators.INFO_STATUS_CHANGE):
            return self.get_text(Locators.INFO_STATUS_CHANGE)






