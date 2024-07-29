from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    return x

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    sss = WebDriverWait(browser, 7).until(EC.text_to_be_present_in_element(("xpath", "//h5[@id='price']"), "100"))

    button = browser.find_element(By.XPATH, "//button[@id='book']").click()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, "//input[@id='answer']")
    input.send_keys(y)
    button1 = browser.find_element(By.XPATH, "//button[@id='solve']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()