# -*- coding: utf-8 -*-

import sys
sys.stdout.reconfigure(encoding='utf-8')


# Функция для проверки, является ли год високосным
def is_year_leap(year):
    return year % 4 == 0


# Вызов функции с конкретным годом
year = 2023  # Замените на любой год, который хотите проверить
result = is_year_leap(year)

# Вывод результата
print(f"Год {year}: {result}")
