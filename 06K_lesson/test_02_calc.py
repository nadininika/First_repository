from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    driver_path = r"C:\Users\nadin\OneDrive\Desktop\first_repository-main" \
              r"\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):
    # Открываем страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    # Устанавливаем задержку 45 секунд
    delay_input = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки 7 + 8 =
    buttons_to_click = ["7", "+", "8", "="]
    for button_text in buttons_to_click:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, f'//span[text()="{button_text}"]'))
        )
        button.click()

    # Ожидаем появления результата в элементе с class="screen"
    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
