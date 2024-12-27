# -*- coding: utf-8 -*-


# Функция fizz_buzz
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Пример вызова функции
number = 17  # Замените на любое значение
fizz_buzz(number)
