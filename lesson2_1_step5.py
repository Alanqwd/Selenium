from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    # val = browser.find_element(By.ID, "#input_value")
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле.
    inp = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    inp.send_keys(y)

    # Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()




    # Нажать на кнопку Submit.
  
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)

finally:
    time.sleep(3)
    browser.quit()