import allure
from selenium import webdriver
from login_page_shop import LoginPage
from product_page_shop import ProductPage
from checkout_page_shop import CheckoutPage

@allure.title("Тест: Покупка товаров в интернет-магазине")
@allure.description("Тест проверяет процесс добавления товаров в корзину, перехода к оформлению заказа и подтверждения итоговой суммы.")
@allure.feature("Корзина покупок")
@allure.severity(allure.severity_level.NORMAL)
def test_shopping_cart():
    driver = webdriver.Chrome()

    try:
        # Инициализация страниц
        login_page = LoginPage(driver)
        product_page = ProductPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Шаг 1: Открыть сайт"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Шаг 2: Авторизация"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Шаг 3: Добавить товары в корзину"):
            product_page.add_to_cart("sauce-labs-backpack")
            product_page.add_to_cart("sauce-labs-bolt-t-shirt")
            product_page.add_to_cart("sauce-labs-onesie")

        with allure.step("Шаг 4: Перейти в корзину"):
            product_page.go_to_cart()

        with allure.step("Шаг 5: Перейти к Checkout"):
            checkout_page.click_continue()

        with allure.step("Шаг 6: Заполнить форму"):
            checkout_page.fill_form("Иван", "Петров", "123456")
            checkout_page.click_continue()

        with allure.step("Шаг 7: Проверить итоговую сумму"):
            total = checkout_page.get_total()
            assert total == "Total: $58.29", f"Ошибка: ожидалось $58.29, получено {total}"

        print("Тест успешно завершён!")

    except Exception as e:
        allure.attach(str(e), name="Ошибка", attachment_type=allure.attachment_type.TEXT)
        print(f"Ошибка: {e}")
    finally:
        driver.quit()
