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


def test_form(driver):
    # Открываем страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    # Ждём, чтобы страница прогрузилась
    wait = WebDriverWait(driver, 10)

    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажимаем кнопку Submit
    submit_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//button[text()="Submit"]')))
    submit_button.click()

    # Проверяем поле Zip code (учитываем, что оно теперь имеет ID)
    zip_code = driver.find_element(By.ID, "zip-code")
    zip_code_class = zip_code.get_attribute("class")
    print(f"Класс поля Zip code: {zip_code_class}")
    assert "alert-danger" in zip_code_class, \
        "Поле Zip code не подсвечено красным \
            (class='alert-danger' отсутствует)"

    # Проверяем, что остальные поля подсвечены зелёным
    field_ids = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field_id in field_ids:
        field = driver.find_element(By.ID, field_id)
        field_class = field.get_attribute("class")
        print(f"Класс поля {field_id}: {field_class}")
        assert "alert-success" in field_class, \
            f"Поле {field_id} не подсвечено зелёным \
                (class='alert-success' отсутствует)"
