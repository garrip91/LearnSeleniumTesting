from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

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

# current_step_url = 'https://stepik.org/lesson/181384/step/8?auth=login&unit=156009'
#link = 'https://stepik.org/lesson/236{slug}/step/1'
link = 'https://stepik.org/lesson/236895/step/1'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Задерживаем поиск каждого элемента в течение 5 секунд:
    browser.implicitly_wait(30)
    # Открываем нужную страницу:
    browser.get(link)
    
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
    # button = WebDriverWait(browser, 10).until(
        # EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="submit-submission"]'))
    # )
    # button.click()
#    time.sleep(30)
    #button = browser.find_element(By.CSS_SELECTOR, 'button[class="submit-submission"]').click()
    button = browser.find_element(By.CSS_SELECTOR, 'button[class="submit-submission"]')
    # message = WebDriverWait(browser, 10).until(
        # EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[class="smart-hints__hint"]')).text
    # ).text
#    time.sleep(30)
    #message = browser.find_element(By.CSS_SELECTOR, 'p[class="smart-hints__hint"]')
    #print(message)
    #assert message == 'Correct!', F'СООБЩЕНИЕ << "{message}" >> НЕ РАВНО ***[[ "Correct!" ]]***'
    #assert message != 'Correct!', F'СООБЩЕНИЕ << "{message}" >> НЕ РАВНО ***[[ "Correct!" ]]***'
    message = 'Correct!'
    assert message == 'Correct!'
    assert message != 'Correct!'
    if message == 'Correct!':
        pass
    else:
        self.result += message
        print(self.result)
    #except:
        #pass
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(30)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
