# ЗАПУСКАТЬ КОД С ФЛАГАМИ  "-s -v"!
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from selenium.common.exceptions import NoSuchElementException

# import os
# from pathlib import Path
# import environ


# !!! НАПОМИНАЛКА: ОБЯЗАТЕЛЬНО УТОЧНИТЬ ПОЧЕМУ @pytest.mark.skipif()...
# ...НЕ БЕРЁТ 'browser' ИЗ conftest.py !!!
@pytest.fixture(scope='session')
#@pytest.fixture(scope='module')
#@pytest.fixture(scope='class')
#@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


def test_pieces_of_the_message(browser):
    link = 'https://stepik.org/lesson/236895/step/1'
    browser.get(link)
    browser.implicitly_wait(10)
    
    try:
        import os
        from pathlib import Path
        import environ
        # ПУТЬ ВЗЯТ ИЗ ".../LearnSeleniumTesting/src/2._Useful_Selenium_methods/2.2._Working_with_files,_lists_and_js-scripts/try_os_path.py":
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        env = environ.Env(
            # set casting, default value:
            DEFAULT=(bool, False)
        )
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
        current_step_url = link
        button = browser.find_element(By.CSS_SELECTOR, 'a[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]')
        button.click()
        time.sleep(10)
        email = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_email"]').send_keys(env('EMAIL'))
        password = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_password"]').send_keys(env('PASSWORD'))
        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    except:
        pass
    
    time.sleep(10)
    
    try:
        button = browser.find_element(By.CSS_SELECTOR, 'button[class="again-btn white"]')
    except NoSuchElementException:
        print('КНОПКИ НЕТ!')
    else:
        print('КНОПКА ЕСТЬ!')
    time.sleep(10)
