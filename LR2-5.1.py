def sum_of_digits(num):
    return sum(int(d) for d in str(num))

n = int(input("Введите число: "))
count = 0

while n != 0:
    n = n - sum_of_digits(n)
    count += 1

print("Количество действий до получения нуля:", count)
