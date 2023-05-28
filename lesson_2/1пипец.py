day = "28"
month = "05"
year = "2023"
day = int(input("Введите день своего рождения: "))
month = int(input("Введите месяц своего рождения: "))
year = int(input("Введите год своего рождения: "))
if day < 1 or day > 31: print("Ошибка: неверный день рождения")
elif month < 1 or month > 12: print("Ошибка: неверный месяц рождения")
elif year > 2022: print("Ошибка: неверный год рождения")
if 2022 - year > 18: print("путь открыт")
elif 2022 - year == 18 and month < 12: print("путь открыт")
elif 2022 - year == 18 and month == 12 and day <= 31: print("путь открыт")
else: print("куда лезешь малой")