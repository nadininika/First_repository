from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class BasePage:
    """
    Базовый класс для всех страниц.
    """

    def __init__(self, driver):
        """
        Инициализирует базовую страницу.

        Аргументы:
            driver (WebDriver): Экземпляр драйвера Selenium.
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Ожидание элемента на странице")
    def wait_for_element(self, by: str, value: str):
        """
        Ожидает, пока элемент станет видимым на странице.

        Аргументы:
            by (str): Метод поиска элемента (например, By.ID, By.NAME).
            value (str): Значение, по которому производится поиск элемента.

        Возвращаемое значение:
            WebElement: Найденный элемент.
        """
        return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((by, value)))

class FormPage(BasePage):
    """
    Класс для работы со страницей формы.
    Наследует от BasePage.
    """

    @allure.step("Заполнение формы данными")
    def fill_form(self, data: dict):
        """
        Заполняет форму данными из словаря.

        Аргументы:
            data (dict): Словарь с данными для заполнения формы. Ключи должны совпадать с именами полей формы.

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.NAME, "first-name").send_keys(data["first_name"])
        self._driver.find_element(By.NAME, "last-name").send_keys(data["last_name"])
        self._driver.find_element(By.NAME, "address").send_keys(data["address"])
        self._driver.find_element(By.NAME, "e-mail").send_keys(data["email"])
        self._driver.find_element(By.NAME, "phone").send_keys(data["phone"])
        self._driver.find_element(By.NAME, "zip-code").send_keys(data["zip"])
        self._driver.find_element(By.NAME, "city").send_keys(data["city"])
        self._driver.find_element(By.NAME, "country").send_keys(data["country"])
        self._driver.find_element(By.NAME, "job-position").send_keys(data["job"])
        self._driver.find_element(By.NAME, "company").send_keys(data["company"])

    @allure.step("Отправка формы")
    def submit_form(self):
        """
        Нажимает кнопку для отправки формы.

        Аргументы:
            None

        Возвращаемое значение:
            None
        """
        self._driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    @allure.step("Получение класса поля")
    def get_field_class(self, field_id: str) -> str:
        """
        Возвращает CSS-класс поля формы по его ID.

        Аргументы:
            field_id (str): Идентификатор поля формы.

        Возвращаемое значение:
            str: Значение атрибута class.
        """
        return self._driver.find_element(By.ID, field_id).get_attribute("class")

    @allure.step("Проверка успешного статуса поля")
    def get_field(self, field_id: str):
        """
        Проверяет, подсвечено ли поле зеленым (успешное заполнение).

        Аргументы:
            field_id (str): Идентификатор проверяемого поля.

        Возвращаемое значение:
            None
        """
        field_element = self._driver.find_element(By.ID, field_id)
        assert "success" in field_element.get_attribute("class"), f"Поле {field_id} должно быть подсвечено зеленым."
