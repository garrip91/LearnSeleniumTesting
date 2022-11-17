import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help='Choose browser: Chrome or Firefox')
    #parser.addoption('--browser_name', action='store', default='Chrome', help='Choose browser: Chrome or Firefox')
    parser.addoption('--language', action='store', default=None, help='Choose language: ru, en, es...')
    #parser.addoption('--language', action='store', default='en', help='Choose language: ru, en, es...')

#@pytest.fixture(scope='session')
#@pytest.fixture(scope='module')
#@pytest.fixture(scope='class')
@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'Chrome':
        print(F'\nuser language: {user_language}\nstart {browser_name} browser for test...')
        # ОТДЕЛЬНО ДОБАВЛЕНО:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        #options.add_experimental_option('w3c', False)
        browser = webdriver.Chrome(options=options)
        #######################
        #browser = webdriver.Chrome()
    elif browser_name == 'Firefox':
        print(F'\nuser language: {user_language}\nstart {browser_name} browser for test...')
        # ОТДЕЛЬНО ДОБАВЛЕНО:
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        #######################
        #browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be Chrome or Firefox')
    yield browser
    print('\nquit browser...')
    browser.quit()
