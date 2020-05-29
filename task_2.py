first_number = input("Введіть a\n")
second_number = input("Введіть b\n")

def math(a, b):
    try:
        calculation = (int(first_number) ** 2) / int(second_number)
        return calculation
    except ZeroDivisionError:
        print("Не можемо ділити на 0")
    except ValueError:
        print("Схоже, що щонайменше один аргумент — не число")


print(math(first_number, second_number))




