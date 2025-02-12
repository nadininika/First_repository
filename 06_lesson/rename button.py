from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Инициализация WebDriver для Firefox
driver = webdriver.Firefox()

try:
    # Открыть страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Найти поле ввода и ввести текст "SkyPro"
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Найти синюю кнопку и нажать её
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Ждём обновления текста кнопки
    wait = WebDriverWait(driver, 20)
    wait.until(lambda d: button.text == "SkyPro")

    # Получить текст кнопки
    button_text = button.text
    print(button_text)

finally:
    # Закрыть браузер
    driver.quit()
