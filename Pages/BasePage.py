from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator, *args):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def do_double_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()


    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_move_to_element(self, by_locator, *args):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).move_to_element()

    def find(self, by_locator):
        element = None
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        except:
            print('Элемент не найден')
        return element

    def scroll_to_element(self, by_locator):
        element = self.find(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        pass

    def scroll_down(self, offset=0):
        if offset:
            self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        if offset:
            self.driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def is_visible(self, by_locator):
        element = self.find(by_locator)
        if element:
            return element.is_displayed()
        return False

    def get_text(self, by_locator):
        element = self.find(by_locator)
        text = ''
        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))
        return text

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def finds(self, by_locator):
        elements = []
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        except:
            print("Элементы не найдены")
        return elements

    def count(self, by_locator):
        elements = self.finds(by_locator)
        return len(elements)

    def get_texts(self, by_locator):
        elements = self.finds(by_locator)
        result = []
        for element in elements:
            text = ''
            try:
                text = str(element.text)
            except Exception as e:
                print('Ошибка: {0}'.format(e))
            result.append(text)
        return result

    def get(self, url):
        self.driver.get(url)

    def go_back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()
