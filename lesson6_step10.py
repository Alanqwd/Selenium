from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ВАЖНО: Для сдачи в Stepik оставьте ссылку на registration1.html
link = "http://suninjuly.github.io/registration2.html" 
# link = "http://suninjuly.github.io/registration2.html" # Раскомментируйте, чтобы проверить, что тест падает

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Поле Имя
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Ivan")

    # 2. Поле Фамилия
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Petrov")

    # 3. Поле Email (используем атрибут name, он уникален)
    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@test.com")

    # 4. Кнопка
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    # 5. Проверка успешной регистрации
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    
    # Если текст не совпадает, тест упадет с AssertionError
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Тест прошел успешно на registration1.html!")

finally:
    time.sleep(3)
    browser.quit()