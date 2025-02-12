import allure
from form_page_class import FormPage  # Импорт классов из модуля с описанием страниц

@allure.title("Тест: Заполнение и отправка формы")
@allure.description("Тест проверяет успешное заполнение и отправку формы.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_and_submit_form(driver):
    """
    Тест для проверки формы на корректное заполнение и отправку.
    """
    form_page = FormPage(driver)

    with allure.step("Открытие формы"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    with allure.step("Заполнение формы"):
        form_page.fill_form({
            "first_name": "Иван",
            "last_name": "Иванов",
            "address": "ул. Ленина, д.1",
            "email": "ivanov@example.com",
            "phone": "+79998887766",
            "zip": "123456",
            "city": "Москва",
            "country": "Россия",
            "job": "Инженер",
            "company": "Компания"
        })

    with allure.step("Отправка формы"):
        form_page.submit_form()

    with allure.step("Проверка подсветки полей"):
        for field_id in [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]:
            form_page.get_field(field_id)
