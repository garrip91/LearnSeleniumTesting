from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/math.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    people_radio = browser.find_element(By.ID, 'peopleRule')
    people_checked = people_radio.get_attribute('checked')
    #print(F'value of people radio: {people_checked}')
    #assert people_checked is not None, 'People radio is not selected by default'
    assert people_checked == 'true', 'People radio is not selected by default'
    
    robots_radio = browser.find_element(By.ID, 'robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    assert robots_checked is None
    
    # Отправляем заполненную форму:
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
