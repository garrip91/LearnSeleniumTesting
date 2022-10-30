from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"][class="trollface btn btn-primary"]')
    button.click()
    
    #  ПЕРЕХОД НА НОВУЮ ВКЛАДКУ ПРОИСХОДИТ АВТОМАТИЧЕСКИ!
    
    first_window = browser.window_handles[0]
    print(first_window)
    new_window = browser.window_handles[1]
    print(new_window)
    time.sleep(10)
    browser.switch_to.window(first_window)
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
