from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = 'http://suninjuly.github.io/file_input.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    
    values_dict = {
        1: 'Имя',
        2: 'Фамилия',
        3: 'Почта'
    }
    n = 1
    for element in elements:
        element.send_keys(values_dict[n])
        del values_dict[n]
        n += 1
    
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла
    browser.find_element(By.CSS_SELECTOR, 'input[id="file"]').send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # Успеваем скопировать код за 30 секунд:
    time.sleep(30)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
