from Pages.BasePage import BasePage
from Config.locators import Locators

class CartPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    """Методы связанные с корзиной товаров:"""

    def is_cart_empty(self):
        if self.is_visible(Locators.CART_EMPTY):
            return self.is_visible(Locators.CART_EMPTY)

    def added_to_cart(self):
        self.do_click(Locators.CART_ADD_FIRST_TV)
        self.do_click(Locators.CART_ADD_SECOND_TV)
        self.do_click(Locators.CART_ADD_THIRD_TV)

    def added_to_cart2(self):
        self.do_click(Locators.CART_ADD_FIRST_TV)
        self.do_click(Locators.CART_ADD_SECOND_TV)

    def check_items_to_cart(self):
        self.get_text(Locators.CART_NUMBER_ITEMS)
        return self.get_text(Locators.CART_NUMBER_ITEMS)

    def check_items_to_cart2(self):
        self.get_text(Locators.CART_COUNT_ITEMS)
        return self.get_text(Locators.CART_COUNT_ITEMS)

    def delete_selected_items(self):
        self.do_click(Locators.CART_DELETE_SELECTED_ITEMS)

    def add_plus_item(self):
        self.do_click(Locators.CART_PLUS_ITEM)

    def remove_minus_item(self):
        self.do_click(Locators.CART_MINUS_ITEM)

    def go_to_checkout(self):
        self.do_click(Locators.CART_GO_TO_CHECKOUT)
        return self.is_visible(Locators.CART_BUTTON_CONFIRM)




