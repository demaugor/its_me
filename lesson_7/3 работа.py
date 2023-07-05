import math

choice = input("Введите 'радиус' или 'диаметр': ")

if choice == 'радиус':
    radius = float(input("Введите радиус круга: "))
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    print("Длина окружности:", circumference)
    print("Площадь круга:", area)
elif choice == 'диаметр':
    diameter = float(input("Введите диаметр круга: "))
    radius = diameter / 2
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    print("Длина окружности:", circumference)
    print("Площадь круга:", area)
else:
    print("Некорректный выбор") 