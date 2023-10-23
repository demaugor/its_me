from typing import Any

prise = [(1, 20, 10000), (20, 25, 20000), (25, 30, 25000), (30, 35, 40000),
         (35, 40, 50000), (40, 50, 80000), (50, 55, 120000), (55, 60, 180000),
         (60, 66, 350000)]


def find_prise(level: object, prises: object) -> object:
    for pr in prises:
        if pr[0] <= level < pr[1]:
            return pr[2]

    return -1


while True:
    while True:
        selected_prise = input("Введите уровень: ")
        if not selected_prise:
            print("Список доступных уровней: ", *("-".join(map(str, x[:2])) for x in prise), sep="\n - ")
            continue
        level = int(selected_prise)
        price: int | Any = find_prise(level, prise)
        if price == -1:
            print("Такого уровня нет(ещё)!")
            continue
        break

    multiplier = int(input("множитель: "))
    total_price = price * multiplier
    print(f"\tобщая_цена {total_price}")
