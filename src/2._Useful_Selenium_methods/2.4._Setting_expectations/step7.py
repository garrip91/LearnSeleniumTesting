from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'http://suninjuly.github.io/wait2.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Задерживаем поиск каждого элемента в течение 5 секунд:
    browser.implicitly_wait(5)
    # Открываем нужную страницу:
    browser.get(link)
    
    # Проверяем в течение 5 секунд, пока кнопка не станет кликабельной:
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'verify'))
    )
    # # Проверяем в течение 5 секунд, пока кнопка не станет неактивной:
    # button = WebDriverWait(browser, 5).until_not(
        # EC.element_to_be_clickable((By.ID, "verify"))
    # )
    button.click()
    message = browser.find_element(By.ID, 'verify_message')
    
    assert 'successful' in message.text
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    #time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
