from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    # Находим первое слагаемое:
    num1 = browser.find_element(By.CSS_SELECTOR, 'span[id="num1"]').text
    # Находим второе слагаемое:
    num2 = browser.find_element(By.CSS_SELECTOR, 'span[id="num2"]').text
    # Суммируем их:
    num_sum = int(num1) + int(num2)
    print(num_sum)
    
    # browser.find_element(By.TAG_NAME, 'select').click()
    # #browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    # for element in browser.find_elements(By.CSS_SELECTOR, 'option'):
        # if element.text == F'{str(num_sum)}':
            # element.click()
    
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(F'{str(num_sum)}') # ищем элемент с нужным текстом
    
    # Отправляем заполненную форму:
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
