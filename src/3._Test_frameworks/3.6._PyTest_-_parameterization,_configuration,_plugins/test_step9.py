# КОД ЗАПУСКАТЬ С ФЛАГАМИ  "-s -v"!
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import math

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# # !!! НАПОМИНАЛКА: ОБЯЗАТЕЛЬНО УТОЧНИТЬ ПОЧЕМУ...
# # ...НЕ БЕРЁТ 'browser' ИЗ conftest.py !!!
# @pytest.fixture(scope='session')
# #@pytest.fixture(scope='module')
# #@pytest.fixture(scope='class')
# #@pytest.fixture(scope='function')
# def browser():
    # print('\nstart browser for test..')
    # browser = webdriver.Chrome()
    # yield browser
    # print('\nquit browser..')
    # browser.quit()


class TestResult:
    
    def test_pieces_of_the_message(self, browser, language):
        link = F'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
        browser.get(link)
        browser.implicitly_wait(10)
        
        time.sleep(30)