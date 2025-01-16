from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Укажите путь к вашему WebDriver
driver_path = (
    "C:/Users/nadin/OneDrive/Desktop/first_repository-main/"
    "05_lesson/chromedriver.exe"
)

# Создаём объект Service
service = Service(driver_path)

# Инициализируем WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Шаг 1: Открыть страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Шаг 2: Найти синюю кнопку по CSS-классу и кликнуть
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()

    # Шаг 3: Вывести сообщение об успешном клике
    print("Клик по синей кнопке выполнен успешно.")

finally:
    # Закрыть браузер
    driver.quit()
