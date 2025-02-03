from base_page3 import BasePage3
from selenium.webdriver.common.by import By

class LoginPage(BasePage3):
    def enter_username(self, username):
        self.send_keys(By.ID, "user-name", username)

    def enter_password(self, password):
        self.send_keys(By.ID, "password", password)

    def click_login(self):
        self.click(By.XPATH, "//input[@type='submit']")
