from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    bt = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    bt.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    num = browser.find_element(By.CSS_SELECTOR, "#input_value")
    numb = int(num.text)
    res = math.log(abs(12 * math.sin(numb)))

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(f'{res}')

    bt = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    bt.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

