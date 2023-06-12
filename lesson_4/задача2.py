import random

i = random.randint(1, 100)
user = 0

while user != i:
    user = int(input("Угадай число от 1 до 100: "))
    if user > i:
        print("Число должно быть меньше")
    elif user < i:
        print("Число должно быть больше")
    else:
        print("Вы угадали число!")