from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'https://stepik.org/catalog'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, 'a[class="ember-view navbar__auth navbar__auth_login st-link st-link_style_button"]')
    button.click()
    time.sleep(20)
    login_email = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_email"]').send_keys('garrip91@yandex.ru')
    login_password = browser.find_element(By.CSS_SELECTOR, 'input[id="id_login_password"]').send_keys('pass737862')
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    time.sleep(20)
    browser.get('https://stepik.org/lesson/184253/step/4?auth=login&unit=158843')
    time.sleep(20)
    # Скроллим страницу вниз для доступности нужных поля и кнопки:
    #browser.execute_script('window.scrollTo(0, 600)')
    h3 = browser.find_element(By.CSS_SELECTOR, 'h3[class="quiz__typename"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", h3)
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
