import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    #parser.addoption('--browser_name', action='store', default=None, help='Choose browser: Chrome or Firefox')
    parser.addoption('--browser_name', action='store', default='Chrome', help='Choose browser: Chrome or Firefox')
    parser.addoption('--language', action='store', default='ru', help='Choose language: ec or fr')

#@pytest.fixture(scope='session')
#@pytest.fixture(scope='module')
#@pytest.fixture(scope='class')
@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'Chrome':
        print('\nstart Chrome browser for test..')
        browser = webdriver.Chrome()
    elif browser_name == 'Firefox':
        print('\nstart Firefox browser for test..')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be Chrome or Firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()
    
    options = Options()
    #user_language = 'en'
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    #options.add_experimental_option('prefs', {'intl.accept_languages': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'})
    browser = webdriver.Chrome(options=options)
