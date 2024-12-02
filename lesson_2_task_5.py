# lesson_2_task_5.py


# Функция для определения сезона по номеру месяца
def month_to_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month number"


# Пример вызова функции
month_number = 5  # Замените на любой номер месяца
season = month_to_season(month_number)

# Вывод результата
print(f"Month {month_number} belongs to the season: {season}")
