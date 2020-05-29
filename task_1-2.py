def oops_2():
    try:
        print(1 / 0)
    except Exception as exc:
        raise IndexError("Вибач, але у нас помилка")


oops_2()