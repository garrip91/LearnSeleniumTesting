from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = 'http://suninjuly.github.io/get_attribute.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    def calc(x: str) -> str:
        return str(math.log(abs(12*math.sin(int(x)))))
    
    # Находим элемент-картинку и извлекаем из него нужное нам число в строковом представлении:
    x_element = browser.find_element(By.CSS_SELECTOR, 'img[id="treasure"]')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    
    # Находим и заполняем нужное поле:
    answer = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]').send_keys(y)
    
    # Находим и ставим галочку в чекбоксе:
    robotCheckbox = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]').click()
    
    # Находим и выбираем нужную нам радио-кнопку:
    robotsRule = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]').click()
    
    # Отправляем заполненную форму:
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()