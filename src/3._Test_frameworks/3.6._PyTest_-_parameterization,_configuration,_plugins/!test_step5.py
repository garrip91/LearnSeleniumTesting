# КОД ЗАПУСКАТЬ С ФЛАГАМИ  "-s -v"!
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import math

from selenium.common.exceptions import NoSuchElementException


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


class TestResult:
    
    result = ''
    slugs = ['895']
    #slugs = ['895', '896', '897', '898', '899', '903', '904', '905']
    
    @pytest.mark.parametrize('slug', slugs)
    def test_pieces_of_the_message(self, browser, slug):
        link = F'https://stepik.org/lesson/236{slug}/step/1'
        #math.log(int(time.time())) = math.log(int(time.time()))
        browser.get(link)
        browser.implicitly_wait(10)
        
        try:
            import os
            from pathlib import Path
            import environ
            BASE_DIR = Path(__file__).resolve().parent.parent.parent
            env = environ.Env(
                DEFAULT=(bool, False)
            )
            environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
            button1 = browser.find_element(By.CSS_SELECTOR, 'a[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]').click()
            email = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_email"]').send_keys(env('EMAIL'))
            password = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_password"]').send_keys(env('PASSWORD'))
            button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        except:
            pass
        
        
        try:
            button3 = browser.find_element(By.CSS_SELECTOR, 'button[class="again-btn white"]')
        except NoSuchElementException:
            print('КНОПКИ СБРОСА ОТПРАВЛЕННОГО ЗНАЧЕНИЯ НЕТ!')
            browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(str(math.log(int(time.time()))))
            button4 = browser.find_element(By.CSS_SELECTOR, 'button[class="submit-submission"]').click()
        # else:
            # print('КНОПКА СБРОСА ОТПРАВЛЕННОГО ЗНАЧЕНИЯ ЕСТЬ!')
            # # СБРОС ОТПРАВЛЕННОГО ЗНАЧЕНИЯ:
            # # browser.get(link)
            # time.sleep(10)
            # button3 = browser.find_element(By.CSS_SELECTOR, 'button[class="again-btn white"]').click()
            # time.sleep(10)
            # button4 = browser.find_elements(By.CSS_SELECTOR, 'button[type="button"]')
            # time.sleep(10)
            # for element in button4:
                # if element.text == 'OK':
                    # element.click()
                    # time.sleep(10)
                    # print('КНОПКА СБРОСА ОТПРАВЛЕННОГО ЗНАЧЕНИЯ ИСЧЕЗЛА!')
                    # time.sleep(10)
                    # browser.get(link)
                    # time.sleep(10)
                    # browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(str(math.log(int(time.time()))))
                    # time.sleep(10)
                    # button4 = browser.find_element(By.CSS_SELECTOR, 'button[class="submit-submission"]').click()
                    # time.sleep(10)
        
        
        
        
        # БЛОК С ПРАВИЛЬНЫМ ИЛИ НЕПРАВИЛЬНЫМ ТЕКСТОМ:
        smart_hints_text = browser.find_element(By.CSS_SELECTOR, 'p[class="smart-hints__hint"]').text
        
        
        if smart_hints_text == 'Correct!':
            print('STRING VALUE MATCH!')
            print(F'smart_hints_text IS ***[[ {smart_hints_text} ]]***')
            result += smart_hints_text
        else:
            print('STRING VALUE MISMATCH!')
            print(F'smart_hints_text IS ***[[ {smart_hints_text} ]]***')
            result += smart_hints_text
    
    
    def test_global_result(self, result):
        self.result = result
        print(self.result)
