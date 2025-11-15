from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    firstname.send_keys('Иван')

    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys('Иванов')

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('dfdf@qa.qa')

    file = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file.send_keys(file_path)


    bt = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    bt.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

