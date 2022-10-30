from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/wait1.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    time.sleep(1)
    button = browser.find_element(By.ID, 'verify')
    button.click()
    message = browser.find_element(By.ID, 'verify_message')
    
    assert 'successful' in message.text
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
