from selenium import webdriver
#### Я ДОБАВИЛ: ####
#from selenium.webdriver import ActionChains
####################
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/huge_form.html'

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
        3: 'a@b.c',
        4: 'Страна',
        5: 'Город',
        6: 'Улица',
        7: 'питомцы',
        8: 'фильмы',
        9: 'артисты',
        10: 'альбомы',
        11: 'машины',
        12: 'хобби',
        13: 'книги',
        14: 'спорт',
        15: 'хз',
        16: 'путешествия',
        17: 'Дисней',
        18: '666',
        19: 'кровь',
        20: 'цвет',
        21: 'еда',
        22: 'пирожок',
        23: 'магазин',
        24: 'радио',
        25: 'актёр',
        26: 'актриса',
        27: 'текст_1',
        28: 'текст_2',
        29: 'текст_3',
        30: 'текст_4',
        31: 'текст_5',
        32: 'текст_6',
        33: 'текст_7',
        34: 'текст_8',
        35: 'текст_9',
        36: 'текст_10',
        37: 'текст_11',
        38: 'текст_12',
        39: 'текст_13',
        40: 'текст_14',
        41: 'текст_15',
        42: 'текст_16',
        43: 'текст_17',
        44: 'текст_18',
        45: 'текст_19',
        46: 'текст_20',
        47: 'текст_21',
        48: 'текст_22',
        49: 'текст_23',
        50: 'текст_24',
        51: 'текст_25',
        52: 'текст_26',
        53: 'текст_27',
        54: 'текст_28',
        55: 'текст_29',
        56: 'текст_30',
        57: 'текст_31',
        58: 'текст_32',
        59: 'текст_33',
        60: 'текст_34',
        61: 'текст_35',
        62: 'текст_36',
        63: 'текст_37',
        64: 'текст_38',
        65: 'текст_39',
        66: 'текст_40',
        67: 'текст_41',
        68: 'текст_42',
        69: 'текст_43',
        70: 'текст_44',
        71: 'текст_45',
        72: 'текст_46',
        73: 'текст_47',
        74: 'текст_48',
        75: 'текст_49',
        76: 'текст_50',
        77: 'текст_51',
        78: 'текст_52',
        79: 'текст_53',
        80: 'текст_54',
        81: 'текст_55',
        82: 'текст_56',
        83: 'текст_57',
        84: 'текст_58',
        85: 'текст_59',
        86: 'текст_60',
        87: 'текст_61',
        88: 'QA/QC',
        89: 'jira/teamcity',
        90: 'severity/priority',
        91: 'bug/defect',
        92: 'python/java',
        93: 'python',
        94: 'selenium',
        95: 'pigeons',
        96: 'pinguins',
        97: 'Trump',
        98: 'yellow',
        99: 'harry potter',
        100: 'socks'
    }
    n = 1
    for element in elements:
        element.send_keys(values_dict[n])
        del values_dict[n]
        n += 1
        #time.sleep(5)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # Успеваем скопировать код за 30 секунд:
    time.sleep(30)
    # Закрываем браузер после всех манипуляций:
    browser.quit()
