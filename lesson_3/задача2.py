import random

N = random.randint(1, 100)
user = 15

while user != N:
    user = int(input("Угадай число от 1 до 100: "))
    if user > N:
        print("Число должно быть меньше")
    elif user < N:
        print("Число должно быть больше")
    else:
        print("Вы угадали число!")