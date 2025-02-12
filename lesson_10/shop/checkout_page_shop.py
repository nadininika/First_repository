from selenium.webdriver.common.by import By
from base_page_shop import BasePage

class CheckoutPage(BasePage):
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму на странице оформления заказа.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        :return: None.
        """
        self.send_keys(By.ID, "first-name", first_name)
        self.send_keys(By.ID, "last-name", last_name)
        self.send_keys(By.ID, "postal-code", postal_code)

    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения на странице оформления заказа.

        :return: None.
        """
        self.click(By.XPATH, "//input[@type='submit']")

    def get_total(self) -> str:
        """
        Получает итоговую сумму с страницы.

        :return: Возвращает строку с итоговой суммой.
        """
        return self.get_text(By.CSS_SELECTOR, ".summary_total_label")
