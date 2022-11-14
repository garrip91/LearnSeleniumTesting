# КОД ЗАПУСКАТЬ С ФЛАГАМИ  "-s -v"!
import pytest

#import unittest
#from parameterized import parameterized

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import math

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
            button = browser.find_element(By.CSS_SELECTOR, 'a[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]').click()
            email = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_email"]').send_keys(env('EMAIL'))
            password = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_password"]').send_keys(env('PASSWORD'))
            button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        except:
            pass
        
        
        #try:
        textarea = browser.find_element(By.CSS_SELECTOR, 'textarea')
        textarea.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="submit-submission"]'))
        )
        button.click()
        message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[class="smart-hints__hint"]')).text
        )
        print(message)
        #assert message == 'Correct!', F'СООБЩЕНИЕ << "{message}" >> НЕ РАВНО ***[[ "Correct!" ]]***'
        #assert message != 'Correct!', F'СООБЩЕНИЕ << "{message}" >> НЕ РАВНО ***[[ "Correct!" ]]***'
        assert message == 'Correct!'
        assert message != 'Correct!'
        if message == 'Correct!':
            pass
        else:
            self.result += message
            print(self.result)
        #except:
            #pass
        
        #button4 = browser.find_element(By.CSS_SELECTOR, 'button[class="submit-submission"]').click()
    
    
    
    
    # # БЛОК С ПРАВИЛЬНЫМ ИЛИ НЕПРАВИЛЬНЫМ ТЕКСТОМ:
    # smart_hints_text = browser.find_element(By.CSS_SELECTOR, 'p[class="smart-hints__hint"]').text
    
    
    # if smart_hints_text == 'Correct!':
        # print('STRING VALUE MATCH!')
        # print(F'smart_hints_text IS ***[[ {smart_hints_text} ]]***')
        # result += smart_hints_text
    # else:
        # print('STRING VALUE MISMATCH!')
        # print(F'smart_hints_text IS ***[[ {smart_hints_text} ]]***')
        # result += smart_hints_text


# def test_global_result(self, result):
    # self.result = result
    # print(self.result)


# if __name__ == '__main__':
    # unittest.main()
