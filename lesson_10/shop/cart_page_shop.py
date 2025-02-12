from selenium.webdriver.common.by import By
import allure
from base_page_shop import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Удаление товара из корзины")
    def remove_item(self, product_id: str):
        self.click(By.CSS_SELECTOR, f'.cart_button[data-product-id="{product_id}"]')

    @allure.step("Получение общей суммы заказа")
    def get_total(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
