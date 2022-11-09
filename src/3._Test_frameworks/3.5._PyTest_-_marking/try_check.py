# ЗАПУСКАТЬ КОД С ФЛАГАМИ: ' -s -v -m "..." ....py'!
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link1 = 'http://selenium1py.pythonanywhere.com/'
link2 = 'https://design.megagroup.ru/solution/3283544'
link3 = 'https://kupislona-store.ru/'
link4 = 'https://hidogs.ru/'


# @pytest.fixture(scope='function')
# def browser():
    # print('\nstart browser for test..')
    # browser = webdriver.Chrome()
    # yield browser
    # print('\nquit browser..')
    # browser.quit()


@pytest.mark.mark1
class TestMainPage1():
    
    @pytest.mark.mark2
    def test_guest_should_see_login_link(self, browser):
        browser.get(link1)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
    
    @pytest.mark.mark3
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link2)
        browser.find_element(By.CSS_SELECTOR, 'h1[class="mp-catalog__title"]')
    
    @pytest.mark.mark4
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link3)
        browser.find_element(By.CSS_SELECTOR, 'div[id="header_menu"]')

@pytest.mark.mark5
def test_main_page(browser):
    browser.get(link4)
    browser.find_element(By.CSS_SELECTOR, 'div[class="td-header-sp-logo"]')
