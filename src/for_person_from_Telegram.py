from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link1 = 'https://replit.com/@LilJuiceBox491/Discord-Nitro-Proof-Bot'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Задерживаем поиск каждого элемента в течение 5 секунд:
    browser.implicitly_wait(10)
    # Открываем нужную страницу:
    browser.get(link1)
    #browser.implicitly_wait(3)
    
    #browser.find_element(By.CLASS_NAME, 'css-c0zsqc').click()
    element1 = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="css-frmn7b"] button[class="css-c0zsqc"]')), 'It does not exist on the page!').click()
    
    browser.implicitly_wait(3)
    
    # link2 = WebDriverWait(browser, 3).until(
        # EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="css-frmn7b"] button[class="css-c0zsqc"]')), 'It does not exist on the page!')
    link2 = browser.find_elements(By.CSS_SELECTOR, 'div[class="css-133dlsl"] div[class="css-m48s5x"] a[class="css-wzynpy"]')
    
    #print(len(link2))
    
    # for i in link2:
        # link3 = i.get_attribute('href')
        # print(link3)
    
    browser.implicitly_wait(10)
    
    links = []
    for i in range(len(link2)):
        links.append(link2[i].get_attribute('href'))
    #print(links)
    
    browser.implicitly_wait(10)
    
    for link in links:
        browser.implicitly_wait(3)
        browser.get(link)
        print(link)
    
    #print(links)
    
finally:
    # Ожидаем 120 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(120)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
    pass
