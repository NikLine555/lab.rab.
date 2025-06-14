n = int(input("Введите число n: "))

for i in range(1, 1000):  # берем достаточно большой диапазон
    square = i * i
    if square > n:
        print("Первое число из последовательности квадратов, большее n:", square)
        break
