while True:
    day = int(input("Введите день: ")) # Ввод значения
    month = int(input("Введите месяц: "))  # Ввод значения
    if day < 32 and month < 13:
        if 3 <= month <= 5:
            print("Весна")
            break
        elif 6 <= month <= 8:
            print("Лето")
            break
        elif 9 <= month <= 11:
            print("Осень")
            break
        else:
            print("Зима")
            break
