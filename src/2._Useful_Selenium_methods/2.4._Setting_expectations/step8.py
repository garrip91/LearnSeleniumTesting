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

current_step_url = 'https://stepik.org/lesson/181384/step/8?auth=login&unit=156009'
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Задерживаем поиск каждого элемента в течение 5 секунд:
    browser.implicitly_wait(30)
    # Открываем нужную страницу:
    browser.get(link)
    
    # Проверяем в течение 12 секунд, пока цена не упадёт до $100:
    #price = WebDriverWait(browser, 12).until(
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    if price:
        button = browser.find_element(By.CSS_SELECTOR, 'button[id="book"]').click()
    
    def calc(x: str) -> str:
        return str(math.log(abs(12*math.sin(int(x)))))
    
    # Находим элемент и извлекаем из него нужное нам число в строковом представлении:
    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
    y = calc(x)
    
    # Находим и заполняем нужное поле:
    answer = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]').send_keys(y)
    
    # Отправляем заполненную форму:
    #button = browser.find_element(By.CSS_SELECTOR, 'XYZ')
    button = browser.find_element(By.CSS_SELECTOR, 'button[id="solve"]')
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
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(30)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
