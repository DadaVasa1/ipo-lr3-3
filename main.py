day = int(input("Введите день: ")) # Ввод значения
month = int(input("Введите месяц: "))  # Ввод значения
if not (1 <= month <= 12 and 1 <= day <= 31):
    print("Неверная дата")
elif 3 <= month <= 5:
    print("Весна")
elif 6 <= month <= 8:
    print("Лето")
elif 9 <= month <= 11:
    print("Осень")
else:
    print("Зима")

