import pytest
from selenium import webdriver
#from selenium.webdriver.common.by import By


#@pytest.fixture(scope='session')
#@pytest.fixture(scope='module')
#@pytest.fixture(scope='class')
@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()
