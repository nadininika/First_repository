from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Укажите путь к ChromeDriver
driver_path = (
    "C:/Users/nadin/OneDrive/Desktop/first_repository-main/"
    "chromedriver/chromedriver.exe"
)

# Создаём объект Service
service = Service(driver_path)

# Инициализируем WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Шаг 1: Открыть страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Шаг 2: Пять раз кликнуть на кнопку "Add Element"
    add_button = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
    for _ in range(5):
        add_button.click()

    # Шаг 3: Собрать список кнопок "Delete"
    delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

    # Шаг 4: Вывести размер списка кнопок "Delete"
    print(f"Количество кнопок 'Delete' на странице: {len(delete_buttons)}")

finally:
    # Закрыть браузер
    driver.quit()
