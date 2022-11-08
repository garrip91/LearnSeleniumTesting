# ЗАПУСКАТЬ КОД С ФЛАГАМИ  "-s -v"!
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/'
# Я ДОБАВИЛ:
link2 = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'


#@pytest.fixture
#@pytest.fixture(scope='class')
@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


class TestMainPage1():
    
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print('start test1')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
        print('finish test1')
    
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('start test2')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
        print('finish test2')


# Я ДОБАВИЛ:
def test_my_check_func(browser):
    print('start test3')
    browser.get(link2)
    browser.find_element(By.CSS_SELECTOR, 'a [class="thumbnail"]')
    print('finish test3')
