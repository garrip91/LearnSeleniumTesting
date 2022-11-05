from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

current_step_url = 'https://stepik.org/lesson/138920/step/4?auth=login&unit=196194'
link = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys('Эдуард')
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Мхитарян')
    input3 = browser.find_element(By.NAME, 'firstname')
    input3.send_keys('Москва')
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Россия')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
    ###### ПОЛУЧАЕМ КОНЕЧНОЕ ЗНАЧЕНИЕ И ПЕРЕДАЁМ ЕГО В НУЖНОЕ ПОЛЕ ДЛЯ ЗАЧЁТА ЗАДАНИЯ, ПОСЛЕ ЧЕГО ПРОХОДИМ ЗАДАНИЕ: ######
    time.sleep(30)
    alert = browser.switch_to.alert
    alert_text = alert.text
    result = alert_text.split(': ')[-1]
    alert.accept()
    browser.get('https://stepik.org/catalog')
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, 'a[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]')
    button.click()
    time.sleep(30)
    email = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_email"]').send_keys(env('EMAIL'))
    password = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_password"]').send_keys(env('PASSWORD'))
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    time.sleep(30)
    browser.get(current_step_url)
    time.sleep(30)
    # Определяем заголовок "h3" с классом "quiz__typename", под которым находятся нужные нам поле и кнопка, и скроллим страницу вниз для их доступности:
    h3 = browser.find_element(By.CSS_SELECTOR, 'h3[class="quiz__typename"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", h3)
    answer_textarea = browser.find_element(By.CSS_SELECTOR, 'textarea[class="ember-text-area ember-view textarea string-quiz__textarea"]').send_keys(result)
    button = browser.find_element(By.CSS_SELECTOR, 'button[class="submit-submission"][type="button"]')
    button.click()
    ######################################################################################################################################
    
finally:
    # успеваем скопировать код за 30 секунд:
    time.sleep(30)
    # закрываем браузер после всех манипуляций:
    browser.quit()
