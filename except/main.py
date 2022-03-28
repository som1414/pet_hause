try:
    num = input("Введите число: ")

    if not num.isdigit():
        raise ValueError()
    print(f"Вы ввели {num}")
except ValueError:
    print("Вы ввели неправильное число")
finally:
    print("Выход из программы")
