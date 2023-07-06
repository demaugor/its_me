import math


choice = input("Введите 'радиус' или 'диаметр': ")
try:
    length = float(input('введите значение'))
except:
    print('всё пиздец ты клоун')
    
match choice:
    case v if v in ['радиус', 'r']:
        print(f'''Длина окружности: {2*length*math.pi}
Площадь: {math.pi*(length**2)}''')
    case v if v in ['диаметр', 'd']:
        print(f'''Длина окружности: {length*math.pi}
Площадь: {math.pi*((length/2)**2)}''')
        print(f'''Длина окружности: {length*math.pi}''')
        
    case _: print('чёт говной попахивает')

"""if choice == 'радиус':
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
"""
