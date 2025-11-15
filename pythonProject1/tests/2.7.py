from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    bt = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    bt.click()
    num = browser.find_element(By.CSS_SELECTOR, "#input_value")
    numb = int(num.text)
    res = math.log(abs(12 * math.sin(numb)))

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(f'{res}')

    bt = browser.find_element(By.ID, "solve")
    bt.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




