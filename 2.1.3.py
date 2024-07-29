from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x,y):
    a = str(int(x)+int(y))
    return a

try:
    link2 = "https://suninjuly.github.io/selects1.html"
    browser1 = webdriver.Chrome()
    browser1.get(link2)

    num1 = browser1.find_element(By.XPATH, "//span[@id='num1']")
    num1_text = num1.text
    num2 = browser1.find_element(By.XPATH, "//span[@id='num2']")
    num2_text = num2.text
    result = calc(num1_text,num2_text)
    browser1.find_element(By.XPATH, "//select[@id='dropdown']").send_keys(result)

    browser1.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser1.quit()