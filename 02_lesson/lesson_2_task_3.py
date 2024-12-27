# -*- coding: utf-8 -*-
import sys
import math

sys.stdout.reconfigure(encoding='utf-8')


# Функция для вычисления площади квадрата
def square(side_length):
    # Вычисляем площадь квадрата
    area = side_length ** 2
    # Округляем результат вверх, если он не целый
    return math.ceil(area)


# Пример вызова функции
side = 4.7  # Замените на любое значение стороны квадрата
result = square(side)

# Вывод результата
print(f"Площадь квадрата со стороной {side}: {result}")
