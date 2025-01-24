from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # Перейти на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Дождаться загрузки всех картинок
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape"))
    )

    # Получение значения атрибута src у 3-й картинки
    src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

    # Выводим значение в консоль
    print(src)

finally:
    # Закрытие браузера
    driver.quit()
