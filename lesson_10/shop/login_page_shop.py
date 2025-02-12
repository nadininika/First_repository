from selenium.webdriver.common.by import By
from base_page_shop import BasePage

class LoginPage(BasePage):
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле ввода.

        :param username: Имя пользователя, которое нужно ввести.
        :return: None.
        """
        self.send_keys(By.ID, "user-name", username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле ввода.

        :param password: Пароль, который нужно ввести.
        :return: None.
        """
        self.send_keys(By.ID, "password", password)

    def click_login(self) -> None:
        """
        Нажимает на кнопку логина.

        :return: None.
        """
        self.click(By.XPATH, "//input[@type='submit']")
