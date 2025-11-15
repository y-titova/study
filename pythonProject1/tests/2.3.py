from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    num = browser.find_element(By.CSS_SELECTOR, ".nowrap + #input_value")
    numb = int(num.text)
    res = math.log(abs(12 * math.sin(numb)))
    enter = browser.find_element(By.CSS_SELECTOR, "#answer")
    enter.send_keys(f'{res}')
    ch = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    ch.click()
    rb = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
    rb.click()
    butt = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    butt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

