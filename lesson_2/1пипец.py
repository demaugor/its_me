day = 28
month = 5
year = 2023
day_of_birth = int(input("Введите день своего рождения: "))
month_of_birth = int(input("Введите месяц своего рождения: "))
year_of_birth = int(input("Введите год своего рождения: "))
if day_of_birth < 1 or day_of_birth > 31:
    print("Ошибка: неверный день рождения")
elif month_of_birth < 1 or month_of_birth > 12:
    print("Ошибка: неверный месяц рождения")
elif year_of_birth > 2023: print("Ошибка: неверный год рождения")
if year - year_of_birth > 18: print("путь открыт")
elif year - year_of_birth == 18 and month_of_birth < 12: print("путь открыт")
elif year - year_of_birth == 18 and month_of_birth == 12 and day_of_birth <= 31: print("путь открыт")
else: print("куда лезешь малой")