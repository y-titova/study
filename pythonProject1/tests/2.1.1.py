from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# используем первую страницу для проверки
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # уникальные селекторы для обязательных полей
    first_name = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
    email.send_keys("test@example.com")

    # кнопка отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # проверка успешной регистрации
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations" in welcome_text

finally:
    time.sleep(5)
    browser.quit()