# Ввод числа от пользователя
month_number = int(input("Введите номер месяца (1-12): "))

# Список месяцев на английском
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Проверка корректности ввода и вывод результата
if 1 <= month_number <= 12:
    print("Month:", months[month_number - 1])
else:
    print("Ошибка: введите число от 1 до 12.")
