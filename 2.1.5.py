from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    input1.send_keys("Senior")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
    input2.send_keys("Junior")
    input4 = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    input4.send_keys("Senior.Junior@evraz.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'readme.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)

    browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()