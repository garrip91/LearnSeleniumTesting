# div[class="k9s sk9"] .tk button._4-a1
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'https://www.ozon.ru/category/noutbuki-15692/'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем страницу с категорией товаров "Ноутбуки, планшеты и электронные книги":
    browser.get(link)
    
    #input1 = browser.find_element(By.NAME, 'first_name')
    #input1.send_keys('Эдуард')
    #input2 = browser.find_element(By.NAME, 'last_name')
    #input2.send_keys('Мхитарян')
    #input3 = browser.find_element(By.NAME, 'firstname')
    #input3.send_keys('Москва')
    #input4 = browser.find_element(By.ID, 'country')
    #input4.send_keys('Россия')
    #button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    #button.click()
    
    # Добавляем товары в корзину:
    '''
    for i in range(1, 6):
        add_button = browser.find_element(By.CSS_SELECTOR, f'div[class="k9s sk9"]:nth-child({i}) > .tk button._4-a1')
        add_button.click()
        # Я ДОБАВИЛ:
        #time.sleep(10)
    '''
    add_button1 = browser.find_element(By.CSS_SELECTOR, 'div[class="k9s sk9"]:nth-child(1) > .tk button._4-a1')
    add_button1.click()
    time.sleep(10)
    add_button2 = browser.find_element(By.CSS_SELECTOR, 'div[class="k9s sk9"]:nth-child(2) > .tk button._4-a1')
    add_button2.click()
finally:
    # успеваем скопировать код за 30 секунд:
    time.sleep(30)
    # закрываем браузер после всех манипуляций:
    browser.quit()
    
