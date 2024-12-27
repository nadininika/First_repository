# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')


# lesson_2_task_6.py


# Данный список
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]


# Фильтрация элементов списка
filtered_elements = [
    x for x in lst if x < 30 and x % 3 == 0
]


# Вывод результата
print(
    "Элементы, которые меньше 30 и делятся на 3 без остатка:",
    filtered_elements
)
