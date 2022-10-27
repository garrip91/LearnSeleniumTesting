from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/file_input.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    time.sleep(5)
    #browser.execute_script('alert("Hello!");')
    #browser.execute_script('confirm("Accept or dismiss?");')
    browser.execute_script('prompt("How old are you?");')
    time.sleep(5)
    
    # alert = browser.switch_to.alert
    # alert_text = alert.text
    # print(alert_text)
    # alert.accept()
    # confirm = browser.switch_to.alert
    # confirm_text = confirm.text
    # print(confirm_text)
    # confirm.accept()
    # confirm.dismiss()
    prompt = browser.switch_to.alert
    time.sleep(5)
    prompt.send_keys('Yes!')
    time.sleep(5)
    prompt.accept()
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
