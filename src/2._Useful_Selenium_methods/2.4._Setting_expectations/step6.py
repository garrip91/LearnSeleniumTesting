from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/cats.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Задерживаем поиск каждого элемента в течение 5 секунд:
    browser.implicitly_wait(5)
    # Открываем нужную страницу:
    browser.get(link)
    
    button = browser.find_element(By.ID, 'button')
    button.click()
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    #time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
