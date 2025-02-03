from base_page3 import BasePage3
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage3):
    def fill_form(self, first_name, last_name, postal_code):
        self.send_keys(By.ID, "first-name", first_name)
        self.send_keys(By.ID, "last-name", last_name)
        self.send_keys(By.ID, "postal-code", postal_code)

    def click_continue(self):
        self.click(By.XPATH, "//input[@type='submit']")

    def get_total(self):
        return self.get_text(By.CSS_SELECTOR, ".summary_total_label")
