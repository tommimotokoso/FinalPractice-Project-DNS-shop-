from Pages.BasePage import BasePage

class SearchPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def get_search_page_title(self, title):
        return self.get_title(title)