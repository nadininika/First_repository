from base_page3 import BasePage3
from selenium.webdriver.common.by import By

class ProductPage(BasePage3):
    def add_to_cart(self, product_id):
        self.click(By.CSS_SELECTOR, f'#add-to-cart-{product_id}')

    def go_to_cart(self):
        self.click(By.XPATH, "//a[@class='shopping_cart_link']")
