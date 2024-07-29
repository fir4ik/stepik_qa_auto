from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    return x

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[@class='trollface btn btn-primary']").click()
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, "//input[@id='answer']")
    input.send_keys(y)

    button1 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()