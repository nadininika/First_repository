from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver для Firefox (Selenium Manager автоматически найдет драйвер)
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Явное ожидание появления поля ввода
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    # Ввести текст "1000" в поле ввода
    wait = WebDriverWait(driver, 10)
    input_field.send_keys("1000")
    print("Текст '1000' введен.")

    # Очистить поле ввода
    input_field.clear()
    print("Поле ввода очищено.")

    # Ввести текст "999" в поле ввода
    input_field.send_keys("999")
    print("Текст '999' введен.")

finally:
    # Закрыть браузер
    driver.quit()
