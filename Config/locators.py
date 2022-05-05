from selenium.webdriver.common.by import By

class Locators:

    """Локаторы для логина/разлогина (много динамических ID, поэтому многие локаторы по классу):"""

    BUTTON_SIGNUP = (By.CLASS_NAME, "button-ui.button-ui_white.header__login_button")
    BUTTON_SIGNUP_WITH_PASS = (By.CLASS_NAME, "base-button-container.base-button-container_blue")
    FIELD_EMAIL = (By.XPATH, "//div[2]/div/input")
    FIELD_PASSWORD = (By.XPATH, "//div[3]/div/input")
    BUTTON_LOGIN_HOMEPAGE = (By.CLASS_NAME, "base-ui-button.base-ui-button_brand.base-ui-button_big-flexible-width")
    CLICK_PIC = (By.ID, "user-menu")
    USER_PROFILE_SETTINGS = (By.CLASS_NAME, "user-profile__settings")
    LOGO_LOGOUT = (By.CLASS_NAME, "logo-container__logout")
    LOGIN_ERROR_WRONG_FIELD = (By.CLASS_NAME, "error-message-block.form-entry-with-password__error")
    LOGIN_ASK_ICON = (By.CLASS_NAME, "form-entry-with-password__ask-icon")
    LOGIN_AUTH_TOOLTIP = (By.CLASS_NAME, "auth-tooltip")
    BUTTON_ICON_HIDE_PASSWORD = (By.CLASS_NAME, "form-entry-with-password__password-icon")
    HIDDEN_PASSWORD = (By.CSS_SELECTOR, "input[type=password]")
    OPEN_PASSWORD = (By.CSS_SELECTOR, "input[type=text]")
    FORGOTTEN_PASSWORD = (By.CLASS_NAME, "form-entry-with-password__question")
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, "//div[2]/div/div/div/div[3]/div/div")
    BUTTON_CONFIRM_RECOVERY_PASS = (By.CLASS_NAME, "base-ui-button.base-ui-button_brand.base-ui-button_big-flexible-width")
    FIELD_RECOVERY_ERROR_WRONG = (By.CLASS_NAME, "error-message-block.password-recovery-form__error")

    """Локаторы для функции поиска:"""

    FIELD_SEARCH = (By.XPATH, "//header/nav/div/div[1]/form/div/input")
    BUTTON_SEARCH = (By.XPATH, "//header/nav/div/div[1]/form/div/div[2]/span[2]")
    TITLE_PRODUCT = (By.XPATH, "/html/body/div[1]/div/div[1]/h1")
    LIST_PRODUCT = (By.CSS_SELECTOR, "div[data-id=product]")
    SEARCH_INCORRECT = (By.CSS_SELECTOR, "empty-search-results__container-header")

    """Локаторы для функции каталогизирования/сортировки товара:"""

    LINK_TV = (By.LINK_TEXT, "ТВ и мультимедиа")
    LINK_SUB_TV = (By.LINK_TEXT, "Телевизоры и аксессуары")
    LINK_SUB_SUB_TV = (By.LINK_TEXT, "Телевизоры")
    DESCRIPTION_TV = (By.XPATH, "/html/body/div[1]/div/div[1]/h1")
    SWITCH_PRICE100 = (By.XPATH, "//div[5]/div/div/div[3]/label[6]/span[2]")
    DELETE_PRICE = (By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[1]/div[5]/div/div/div[3]/a")
    TABS_BAR_DIAGONAL = (By.XPATH, "//div/div[3]/div[1]/div[8]/a/i")
    SWITCH_DIAGONAL55 = (By.XPATH, "//div[1]/div[8]/div/div/div[3]/label[6]/span")
    TABS_SMART_TV = (By.XPATH, "//div[1]/div/div[3]/div[1]/div[10]/a/i")
    SWITCH_SMART_TV = (By.XPATH, "//div[3]/div[1]/div[10]/div/div/div/label[1]/span[2]")
    BUTTON_FILTER_ON = (By.CLASS_NAME, "button-ui.button-ui_brand.left-filters__button")
    BUTTON_FILTER_RESET = (By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div/button[2]")
    LIST_FILTERS = (By.CSS_SELECTOR, "div[class=picked-filter]")
    FIELD_MIN_PRICE = (By.XPATH, "//div[1]/div[5]/div/div/div[1]/input")
    FIELD_MAX_PRICE = (By.XPATH, "//div[1]/div[5]/div/div/div[2]/input")
    FIELD_MIN_DIAGONAL = (By.XPATH, "//div[1]/div[8]/div/div/div[1]/input")
    FIELD_MAX_DIAGONAL = (By.XPATH, "//div[1]/div[8]/div/div/div[2]/input")

    """Локаторы для страницы настроек профиля:"""

    BUTTON_OPEN_PROFILE = (By.CLASS_NAME, "publish-toggle__button.publish-toggle__button_opened-hover")
    BUTTON_CLOSED_PROFILE = (By.CLASS_NAME, "publish-toggle__button.publish-toggle__button_closed-hover")
    INFO_STATUS_CHANGE = (By.CLASS_NAME, "user-settings-info__status-show")
    FIELD_INFO_STATUS = (By.CLASS_NAME, "user-status-pop-up__status-text")
    BUTTON_SAVE_INFO_STATUS = (By.XPATH, "/html/body/div[3]/div/button[2]")
    PROFILE_BUTTON_LOGOUT = (By.CLASS_NAME, "logo-container__logout")
    PROFILE_UNAUTHORIZED = (By.CLASS_NAME, "button-ui.button-ui_brand.button-ui_big.button-ui_unauthorized")

    """Локаторы связанные с функцией корзины для товаров:"""

    CART_EMPTY = (By.CLASS_NAME, "empty-message__title-empty-cart")
    CART_ADD_FIRST_TV = (By.XPATH, "//div[3]/div/div[1]/div[1]/div[4]/button[2]")
    CART_ADD_SECOND_TV = (By.XPATH, "//div[3]/div/div[1]/div[2]/div[4]/button[2]")
    CART_ADD_THIRD_TV = (By.XPATH, "//div[3]/div/div[1]/div[3]/div[4]/button[2]")
    CART_ADD_SMARTPHONE = (By.XPATH, "//div[3]/div/div[1]/div[8]/div[4]/button[2]]")
    CART_NUMBER_ITEMS = (By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[1]/span[1]")
    CART_COUNT_ITEMS = (By.CLASS_NAME, "cart-products-count")
    CART_DELETE_SELECTED_ITEMS = (By.CLASS_NAME, "mass-selection__delete-btn")
    CART_MINUS_ITEM = (By.CLASS_NAME, "count-buttons__icon.count-buttons__icon-minus")
    CART_PLUS_ITEM = (By.CLASS_NAME, "count-buttons__button.count-buttons__button_plus")
    CART_GO_TO_CHECKOUT = (By.CLASS_NAME, "base-ui-button-v2_medium.base-ui-button-v2_brand.base-ui-button-v2_ico-none.base-ui-button-v2.buy-button.base-ui-button-v2")
    CART_BUTTON_CONFIRM = (By.CLASS_NAME, "base-ui-button.apply-button__ui-button.base-ui-button_brand.base-ui-button_big")