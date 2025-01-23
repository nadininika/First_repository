from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver для Firefox (Selenium Manager автоматически найдет драйвер)
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Явное ожидание появления поля username
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Ввести значение "tomsmith" в поле username
    username_field.send_keys("tomsmith")
    print("Значение 'tomsmith' введено в поле username.")

    # Найти и ввести значение "SuperSecretPassword!" в поле password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Значение 'SuperSecretPassword!' введено в поле password.")

    # Найти и нажать кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Кнопка 'Login' нажата.")

finally:
    # Закрыть браузер
    driver.quit()
