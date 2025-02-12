from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement  # Добавить импорт WebElement


class BasePage:
    def __init__(self, driver):
        """
        Инициализация базовой страницы.

        :param driver: webdriver.Chrome или аналогичный драйвер Selenium.
        """
        self.driver = driver

    def wait_for_element(self, by: By, value: str, timeout: int = 10) -> WebElement:
        """
        Ожидает, пока элемент станет видимым.

        :param by: Метод поиска элемента (например, By.ID, By.XPATH).
        :param value: Значение для поиска элемента.
        :param timeout: Время ожидания в секундах (по умолчанию 30).
        :return: Возвращает элемент WebElement, если найден, иначе вызывает TimeoutException.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            raise TimeoutException(f"Элемент с {by}={value} не найден за {timeout} секунд")

    def click(self, by: By, value: str) -> None:
        """
        Ожидает элемент и выполняет клик.

        :param by: Метод поиска элемента (например, By.ID, By.XPATH).
        :param value: Значение для поиска элемента.
        :return: None.
        """
        self.wait_for_element(by, value).click()

    def send_keys(self, by: By, value: str, text: str) -> None:
        """
        Ожидает элемент, очищает его и отправляет текст.

        :param by: Метод поиска элемента (например, By.ID, By.XPATH).
        :param value: Значение для поиска элемента.
        :param text: Текст, который нужно ввести в элемент.
        :return: None.
        """
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by: By, value: str) -> str:
        """
        Ожидает элемент и возвращает его текст.

        :param by: Метод поиска элемента (например, By.ID, By.XPATH).
        :param value: Значение для поиска элемента.
        :return: Текст элемента как строка.
        """
        return self.wait_for_element(by, value).text
