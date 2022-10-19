from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager


link = 'http://suninjuly.github.io/simple_form_find_task.html'

#browser = webdriver.Chrome(ChromeDriverManager().install())
browser = webdriver.Chrome()
try:
    browser.get(link)
    button = browser.find_element(By.ID, 'submit_button')
    button.click()
finally:
    # закрываем браузер после всех манипуляций:
    browser.quit()
