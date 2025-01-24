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


def test_shop(driver):
    # Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")

    # Авторизуемся как standard_user
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем в корзину товары
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.ID, "checkout"))).click()

    # Заполняем форму своими данными
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.ID, "first-name"))).send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Petrov")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Считываем итоговую стоимость
    total = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text

    # Закрываем браузер
    driver.quit()

    # Проверяем, что итоговая сумма равна $58.29
    assert total == "Total: $58.29", \
        f"Ожидалось: 'Total: $58.29', но отображено: {total}"
