from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import unittest


class TestRegistration(unittest.TestCase):
    
    def test_registration_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group first_class"] input[type="text"]')
        input1.send_keys('Имя')
        input2 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group second_class"] input[type="text"]')
        input2.send_keys('Фамилия')
        input3 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group third_class"] input[type="text"]')
        input3.send_keys('Почта')
        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'Should be needed text!')
        time.sleep(10)
        browser.quit()
    
    def test_registration_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group first_class"] input[type="text"]')
        input1.send_keys('Имя')
        input2 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group second_class"] input[type="text"]')
        input2.send_keys('Фамилия')
        input3 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] div[class="form-group third_class"] input[type="text"]')
        input3.send_keys('Почта')
        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'Should be needed text!')
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
