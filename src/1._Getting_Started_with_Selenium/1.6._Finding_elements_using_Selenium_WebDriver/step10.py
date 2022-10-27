from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/registration1.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    # Находим нужные элементы на странице:
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    
    # Заполняем обязательные поля формы значениями из словаря:
    values_dict = {
        1: 'Имя',
        2: 'Фамилия',
        3: 'Почта'
    }
    n = 1
    for element in elements:
        if len(values_dict) == 0:
            break
        else:
            element.send_keys(values_dict[n])
            del values_dict[n]
            n += 1
    
    # Отправляем заполненную форму:
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    
    # Проверяем, что смогли зарегистрироваться и ждём загрузки страницы:
    time.sleep(1)
    
    # Находим элемент, содержащий текст:
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    # Записываем в переменную "welcome_text" текст из элемента "welcome_text_elt":
    welcome_text = welcome_text_elt.text
    
    # С помощью "assert" проверяем совпадает ли ожидаемый текст с текстом на странице сайта:
    assert 'Congratulations! You have successfully registered!' == welcome_text
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
