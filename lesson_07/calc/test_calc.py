import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_page import CalculatorPage
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = (webdriver.Chrome
              (service=ChromeService(ChromeDriverManager().install())))
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    (driver.get
     ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"))
    calc_page = CalculatorPage(driver)

    # Установка задержки
    calc_page.set_delay("45")

    # Нажатие на кнопки
    calc_page.click_button('7')
    calc_page.click_button('+')
    calc_page.click_button('8')
    calc_page.click_button('=')

    # Ожидание результата
    (calc_page.wait_for_text
     (By.CSS_SELECTOR, ".screen", "15", timeout=46))

    # Проверка результата
    result = calc_page.get_result()
    assert int(result) == 15