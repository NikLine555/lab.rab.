n = int(input("Введите число n: "))

current = 1
step = 4

while current <= n:
    current += step
    step += 1

print("Первое число, большее n:", current)
