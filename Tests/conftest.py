import pytest
import time

from selenium import webdriver
from Config.config import TestData


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    web_driver.implicitly_wait(10)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.quit()

