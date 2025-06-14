def read_and_print_reverse():
    num = int(input("Введите число (0 для окончания): "))
    if num == 0:
        return
    read_and_print_reverse()
    print(num)

read_and_print_reverse()
