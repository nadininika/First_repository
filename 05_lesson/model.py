from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver (Selenium Manager сам загрузит Geckodriver)
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Явное ожидание появления модального окна
    wait = WebDriverWait(driver, 10)
    close_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer > p"))
    )

    # Нажимаем на кнопку "Close"
    close_button.click()
    print("Модальное окно закрыто.")
finally:
    # Закрыть браузер
    driver.quit()
