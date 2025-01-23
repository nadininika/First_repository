from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # Переход на сайт
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

    # Установка явного ожидания
    wait = WebDriverWait(driver, 60)  # Таймаут 60 секунд

    # Ожидание появления всех картинок
    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4)

    # Получение всех картинок
    images = driver.find_elements(By.TAG_NAME, "img")

    # Проверяем полную загрузку каждой картинки
    for index, image in enumerate(images):
        wait.until(lambda d: image.get_attribute("naturalWidth") != "0")

    # Получаем значение src у 3-й картинки
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print(f"Значение атрибута src у 3-й картинки: {third_image_src}")

finally:
    driver.quit()
