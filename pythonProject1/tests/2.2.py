from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_el1 = browser.find_element(By.CSS_SELECTOR, "id=num1]")
    numb1 = int(find_el1.text)

    find_el2 = browser.find_element(By.CSS_SELECTOR, "span[id=num2]")
    numb2 = int(find_el2.text)


    res = numb1 + numb2
    text_value = f"{res}"

    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_visible_text(text_value)

    enter = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    enter.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





