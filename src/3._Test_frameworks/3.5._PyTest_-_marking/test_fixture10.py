# ЗАПУСКАТЬ КОД С ФЛАГАМИ  "-s -v -m" И С АРГУМЕНТОМ "smoke"!
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/'
# Я ДОБАВИЛ:
link2 = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


class TestMainPage1():
    
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
    
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')
    
    #@pytest.mark.xfail
    @pytest.mark.xfail(reason='fixing this bug right now')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        # Я ИСПРАВИЛ:
        browser.get(link2)
        browser.find_element(By.CSS_SELECTOR, 'button.favorite')
