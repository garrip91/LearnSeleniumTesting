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
    
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value('1') # ищем элемент с текстом "Python"
    # СПОСОБЫ ПОЛУЧШЕ:
    #select.select_by_visible_text("Python")
    #select.select_by_index(1) # индексация начинается с 0
    
    # Отправляем заполненную форму:
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
