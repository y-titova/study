from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_num = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    num = find_num.text
    y = calc(num)

    enter = browser.find_element(By.CSS_SELECTOR, "#answer")
    enter.send_keys(y)

    ch = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    ch.click()
    rb = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    rb.click()

    bt = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    bt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





