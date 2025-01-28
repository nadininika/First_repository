from selenium import webdriver
from login_page import LoginPage
from product_page import ProductPage
from checkout_page import CheckoutPage

def test_shopping_cart():
    driver = webdriver.Chrome()

    try:
        # Инициализация страниц
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        checkout_page = CheckoutPage(driver)

        # Шаг 1: Открыть сайт
        driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизация
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Шаг 3: Добавить товары в корзину
        product_page.add_to_cart("sauce-labs-backpack")
        product_page.add_to_cart("sauce-labs-bolt-t-shirt")
        product_page.add_to_cart("sauce-labs-onesie")

        # Шаг 4: Перейти в корзину
        product_page.go_to_cart()

        # Шаг 5: Перейти к Checkout
        checkout_page.click_continue()

        # Шаг 6: Заполнить форму
        checkout_page.fill_form("Иван", "Петров", "123456")
        checkout_page.click_continue()

        # Шаг 7: Проверить итоговую сумму
        total = checkout_page.get_total()
        assert total == "Total: $58.29", f"Ошибка: ожидалось $58.29, получено {total}"

        print("Тест успешно завершён!")

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()
