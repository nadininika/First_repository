from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Найти и нажать синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # Увеличиваем таймаут и ждём появления текста
    wait = WebDriverWait(driver, 20)
    green_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content > p"))
    )

    # Получение текста из зеленой плашки
    text = green_box.text
    print(text)

finally:
    # Закрыть браузер
    driver.quit()
