from selenium import webdriver
#### Я ДОБАВИЛ: ####
#from selenium.webdriver import ActionChains
####################
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

current_step_url = 'https://stepik.org/lesson/138920/step/8?auth=login&unit=196194'
link = 'http://suninjuly.github.io/find_xpath_form'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    # goods = browser.find_elements(By.CSS_SELECTOR, '[class*="ajax_block_product "]')
    
    # for i in range(1, len(goods)+1):
        # browser.execute_script("window.scrollTo(0, 600)")
        # add_button_block1 = browser.find_element(By.CSS_SELECTOR, F'ul[class="product_list grid row"] li[class*="ajax_block_product"]:nth-child({i}) a[class="button ajax_add_to_cart_button btn btn-default"]')
        # actions = ActionChains(browser)
        # actions.move_to_element(add_button_block1).click().perform()
        # time.sleep(30)
        # close_window = browser.find_element(By.CSS_SELECTOR, 'div[class="layer_cart_product col-xs-12 col-md-6"] span[class="cross"]')
        # close_window.click()
        # time.sleep(30)
    
    # # Открываем корзину:
    # browser.get('http://automationpractice.com/index.php?controller=order')
    # browser.execute_script("window.scrollTo(0, 500)")
    
    # # Ищем все добавленные товары:
    # cart_goods = browser.find_elements(By.CSS_SELECTOR, 'tbody tr[class*="cart_item "]')
    # time.sleep(30)
    
    # # Выводим в консоль количество товаров, добавленных в корзину:
    # print(len(cart_goods))
    
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    
    values_dict = {
        1: 'Имя',
        2: 'Фамилия',
        3: 'Город',
        4: 'Страна',
    }
    n = 1
    for element in elements:
        element.send_keys(values_dict[n])
        del values_dict[n]
        n += 1
        #time.sleep(5)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
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
    # email = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_email"]').send_keys('garrip91@yandex.ru')
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
    # Успеваем скопировать код за 30 секунд:
    time.sleep(30)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
