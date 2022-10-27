from selenium import webdriver
#### Я ДОБАВИЛ: ####
#from selenium.webdriver import ActionChains
####################
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/find_xpath_form'

try:
    # Подготовка для теста:
    browser = webdriver.Chrome()
    # Открываем нужную страницу:
    browser.get(link)
    
    # goods = browser.find_elements(By.CSS_SELECTOR, '[class*="ajax_block_product "]')
    
    # for i in range(1, len(goods)+1):
        # browser.execute_script("window.scrollTo(0, 600)")
        # add_button_block1 = browser.find_element(By.CSS_SELECTOR, F'ul[class="product_list grid row"] li[class*="ajax_block_product"]:nth-child({i}) a[class="button ajax_add_to_cart_button btn btn-default"]')
        # actions = ActionChains(browser)
        # actions.move_to_element(add_button_block1).click().perform()
        # time.sleep(30)
        # close_window = browser.find_element(By.CSS_SELECTOR, 'div[class="layer_cart_product col-xs-12 col-md-6"] span[class="cross"]')
        # close_window.click()
        # time.sleep(30)
    
    # # Открываем корзину:
    # browser.get('http://automationpractice.com/index.php?controller=order')
    # browser.execute_script("window.scrollTo(0, 500)")
    
    # # Ищем все добавленные товары:
    # cart_goods = browser.find_elements(By.CSS_SELECTOR, 'tbody tr[class*="cart_item "]')
    # time.sleep(30)
    
    # # Выводим в консоль количество товаров, добавленных в корзину:
    # print(len(cart_goods))
    
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    
    values_dict = {
        1: 'Имя',
        2: 'Фамилия',
        3: 'Город',
        4: 'Страна',
    }
    n = 1
    for element in elements:
        element.send_keys(values_dict[n])
        del values_dict[n]
        n += 1
        #time.sleep(5)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    
finally:
    # Успеваем скопировать код за 30 секунд:
    time.sleep(30)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
