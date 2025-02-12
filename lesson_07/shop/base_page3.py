from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage3:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        """Ожидает, пока элемент станет видимым."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            print(f"Элемент не найден: {by} = {value}")
            raise

    def click(self, by, value):
        """Ожидает и кликает по элементу."""
        self.wait_for_element(by, value).click()

    def send_keys(self, by, value, text):
        """Ожидает элемент, очищает и отправляет текст."""
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        """Ожидает элемент и возвращает его текст."""
        return self.wait_for_element(by, value).text
