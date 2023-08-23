prise = {'1-20': 10000, '20-25': 20000, '25-30': 25000, '30-35': 40000,
         '35-40': 50000, '40-50': 80000, '50-55': 120000, '55-60': 180000,
         '60-65': 350000}

while True:
    while True:
        selected_prise = input("Введите уровень (оставьте пустым для вывода списка): ")
        if not selected_prise:
            print("Список доступных уровней: ", *prise.keys(), sep="\n - ")
            continue
        if selected_prise not in prise:
            print("Такого уровня нет(ещё)!")
            continue
        break

    monj = int(input("множетель"))
    total_price = prise[selected_prise] * monj
    print(f"\tобщая_цена {total_price}")