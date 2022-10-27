from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/registration2.html'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    # # Через блок вёрстки страницы, содержащий нужные нам (обязательные к заполнению) поля, находим первое обязательное поле:
    # input1 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group first_class"] input[type="text"]')
    # # Заполняем это обязательное поле формы:
    # input1.send_keys('Имя')
    # # Далее то же самое проделываем со вторым обязательным полем:
    # input2 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group second_class"] input[type="text"]')
    # # ...и заполняем его:
    # input2.send_keys('Фамилия')
    # # Ну и с третьим обязательным полем проделываем то же самое:
    # input3 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group third_class"] input[type="text"]')
    # # ...и заполняем его:
    # input3.send_keys('Почта')
    
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    
    values_dict = {
        1: 'Имя',
        2: 'Почта'
    }
    n = 1
    for element in elements:
        if element.get_attribute('required') == True:
            if len(values_dict) == 0:
                break
            else:
                element.send_keys(values_dict[n])
                del values_dict[n]
                n += 1
        else:
            continue
    
    # # Отправляем заполненную форму:
    # button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    # button.click()
    
    # # Проверяем, что смогли зарегистрироваться и ждём загрузки страницы:
    # time.sleep(1)
    
    # # Находим элемент, содержащий текст:
    # welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    # # Записываем в переменную "welcome_text" текст из элемента "welcome_text_elt":
    # welcome_text = welcome_text_elt.text
    
    # # С помощью "assert" проверяем совпадает ли ожидаемый текст с текстом на странице сайта:
    # assert 'Congratulations! You have successfully registered!' == welcome_text
    
finally:
    # Ожидаем 10 секунд, чтобы визуально оценить результаты прохождения скрипта:
    time.sleep(10)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
