import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calc_page_class import CalculatorPage
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.title("Тестирование медленного калькулятора")
@allure.description("Проверяем корректность вычислений с задержкой в 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver):
    with allure.step("Открываем страницу калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calc_page = CalculatorPage(driver)

    with allure.step("Устанавливаем задержку вычислений в 45 секунд"):
        calc_page.set_delay("45")

    with allure.step("Выполняем сложение 7 + 8"):
        calc_page.click_button('7')
        calc_page.click_button('+')
        calc_page.click_button('8')
        calc_page.click_button('=')

    with allure.step("Ожидаем появления результата 15"):
        calc_page.wait_for_text(By.CSS_SELECTOR, ".screen", "15", timeout=46)

    with allure.step("Проверяем, что результат вычисления равен 15"):
        result = calc_page.get_result()
        assert int(result) == 15, f"Ожидалось 15, но получили {result}"
