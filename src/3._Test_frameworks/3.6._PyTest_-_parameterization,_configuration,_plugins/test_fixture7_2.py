# ЗАПУСКАТЬ КОД С ФЛАГАМИ  "-s -v"!
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.mark.parametrize('language', ['ru', 'en-gb'])
class TestLogin:
    
    def test_guest_should_see_login_link(self, browser, language):
        link = F'http://selenium1py.pythonanywhere.com/{language}/'
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
        # Этот тест запустится 2 раза
    
    def test_guest_should_see_navbar_element(self, browser, language):
        link = F'http://selenium1py.pythonanywhere.com/{language}/'
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, 'div[class="navbar navbar-default navbar-static-top accounts"]')
        # этот тест тоже запустится 2 раза
