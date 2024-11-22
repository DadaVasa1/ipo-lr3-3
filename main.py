while True:
    day = int(input("Введите день: ")) # Ввод значения
    month = int(input("Введите месяц: "))  # Ввод значения
    if month == 9 and  day < 31 and day >= 1  or month == 10  and day <= 31 and day >= 1  or month == 11 and day <= 30 and day >= 1 or\
    month == 12 and day >= 1 and day <= 31 or month == 1 and day <= 31 and day >= 1 or month == 2 and day <= 29 and day >= 1 or\
    month == 6 and day < 31 or month == 7 and day < 32 or month == 8 and day < 32 or\
    month == 3 and day <= 31 and day >= 1 or month == 4 and day <= 30 and day >= 1 or month == 5 and day <= 31 and day >= 1:
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
