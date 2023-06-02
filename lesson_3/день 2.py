num_month = input("Введите номер месяца (1-12): ")

try:
    month = int(num_month)
    if month == 1:
        print("Январь")
    elif month == 2:
        print("Февраль")
    elif month == 3:
        print("Март")
    elif month == 4:
        print("Апрель")
    elif month == 5:
        print("Май")
    elif month == 6:
        print("Июнь")
    elif month == 7:
        print("Июль")
    elif month == 8:
        print("Август")
    elif month == 9:
        print("Сентябрь")
    elif month == 10:
        print("Октябрь")
    elif month == 11:
        print("Ноябрь")
    elif month == 12:
        print("Декабрь")
    else:
        print("Неверный номер месяца")
except ValueError:
    print("Ошибка: введено некорректное значение")