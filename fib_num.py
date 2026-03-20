def main():
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))
    except ValueError:
        print("Ошибка: введите целые числа.")
        return

    if start >= end:
        print("Начало должно быть меньше конца.")
        return

    fib_num = []
    a, b = 0, 1
    while a <= end:
        if a >= start:
            fib_num.append(a)
        a, b = b, a + b

    if fib_num:
        print(" ".join(map(str, fib_num)))
    else:
        print("В заданном диапазоне нет чисел Фибоначчи")


if __name__ == "__main__":
    main()
