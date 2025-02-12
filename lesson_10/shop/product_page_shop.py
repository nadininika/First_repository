from selenium.webdriver.common.by import By
from base_page_shop import BasePage

class ProductPage(BasePage):
    def add_to_cart(self, product_id: str) -> None:
        """
        Добавляет продукт в корзину по его ID.

        :param product_id: ID товара, который нужно добавить в корзину.
        :return: None.
        """
        self.click(By.CSS_SELECTOR, f'#add-to-cart-{product_id}')

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.

        :return: None.
        """
        self.click(By.XPATH, "//a[@class='shopping_cart_link']")
