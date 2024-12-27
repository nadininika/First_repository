from smartphone import Smartphone

# Создаём список для каталога
catalog = []

# Наполняем каталог пятью экземплярами класса Smartphone
catalog.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 7", "+79456789012"))
catalog.append(Smartphone("Huawei", "P50 Pro", "+79567890123"))

# Печатаем каталог в формате <марка> - <модель>. <номер телефона>
for smartphone in catalog:
    print(
        f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}"
        )
