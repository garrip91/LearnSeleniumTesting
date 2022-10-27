from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = 'https://SunInJuly.github.io/execute_script.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    #browser.execute_script("alert('Robots at work');")
    #browser.execute_script("document.title='Script executing';")
    #browser.execute_script('document.title="Script executing";')
    #browser.execute_script("document.title='Script executing';alert('Robots at work');")
    button = browser.find_element(By.TAG_NAME, "button")
    #browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    #browser.execute_script("window.scrollTo(0, 1000)")
    #browser.execute_script("window.scrollBy(0, 1000)")
    
    #// javascript
    #button = document.getElementsByTagName("button")[0];
    #button.scrollIntoView(true);
    
    button.click()
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
