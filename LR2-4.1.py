# Ввод размера массива
N = int(input("Введите количество элементов в массиве: "))

# Ввод элементов массива
arr = []
for i in range(N):
    x = float(input(f"Введите элемент {i+1}: "))
    arr.append(x)

# Поиск минимального по модулю элемента
min_abs_element = arr[0]
for num in arr:
    if abs(num) < abs(min_abs_element):
        min_abs_element = num

print("Минимальный по модулю элемент:", min_abs_element)

# Вывод массива в обратном порядке
print("Массив в обратном порядке:")
for num in reversed(arr):
    print(num)
