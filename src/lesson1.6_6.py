from selenium import webdriver
#### Я ДОБАВИЛ: ####
from selenium.webdriver import ActionChains
####################
from selenium.webdriver.common.by import By
import time


link = 'http://automationpractice.com/index.php?id_category=11&controller=category'

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
    '''
    add_button1 = browser.find_element(By.CSS_SELECTOR, 'div[class="k9s sk9"]:nth-child(1) > .tk button._4-a1')
    add_button1.click()
    time.sleep(10)
    add_button2 = browser.find_element(By.CSS_SELECTOR, 'div[class="k9s sk9"]:nth-child(2) > .tk button._4-a1')
    add_button2.click()
    time.sleep(10)
    '''
    
    goods = browser.find_elements(By.CSS_SELECTOR, '[class*="ajax_block_product "]')
    
    for i in range(1, len(goods)+1):
        browser.execute_script("window.scrollTo(0, 600)")
        add_button_block1 = browser.find_element(By.CSS_SELECTOR, F'ul[class="product_list grid row"] li[class*="ajax_block_product"]:nth-child({i}) a[class="button ajax_add_to_cart_button btn btn-default"]')
        actions = ActionChains(browser)
        actions.move_to_element(add_button_block1).click().perform()
        time.sleep(30)
        close_window = browser.find_element(By.CSS_SELECTOR, 'div[class="layer_cart_product col-xs-12 col-md-6"] span[class="cross"]')
        close_window.click()
        time.sleep(30)
    
    # Открываем корзину:
    browser.get('http://automationpractice.com/index.php?controller=order')
    browser.execute_script("window.scrollTo(0, 500)")
    
    # Ищем все добавленные товары:
    cart_goods = browser.find_elements(By.CSS_SELECTOR, 'tbody tr[class*="cart_item "]')
    time.sleep(30)
    
    # Выводим в консоль количество товаров, добавленных в корзину:
    print(len(cart_goods))
    
finally:
    # Успеваем скопировать код за 30 секунд:
    time.sleep(30)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
