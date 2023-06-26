from datetime import datetime, timedelta

bosses = {
    "arh": {"hours": 4, "minutes": 5},
    "zver": {"hours": 4, "minutes": 5},
    "dekst": {"hours": 5, "minutes": 5},
    "gt": {"hours": 5, "minutes": 5},
    "hugo": {"hours": 5, "minutes": 5},
    "baks": {"hours": 5, "minutes": 5},
    "ent": {"hours": 1, "minutes": 28},
    "kk": {"hours": 2, "minutes": 5},
    "hoz": {"hours": 5, "seconds": 5},
    "yp_v": {"hours": 1, "minutes": 10},
    "yp_les": {"hours": 2, "seconds": 5},
    "ost": {"hours": 2, "seconds": 5},
    "Alfa": {"hours": 2},
    "Samka": {"hours": 2},
    "Termit": {"hours": 2},
    "Zt": {"hours": 2},
    "Fara": {"hours": 2},
}

while True:
    while True:
        selected_boss = input("Введите имя босса (оставьте пустым для вывода списка): ")
        if not selected_boss:
            print("Список доступных боссов: ", *bosses.keys(), sep="\n - ")
            continue
        if selected_boss not in bosses:
            print("Такого босса нет!")
            continue
        break

    while True:
        boss_died_at = list(
            map(
                int,
                input(
                    f"Введите время когда умер босс '{selected_boss}' (h:m:s): "
                ).split(":"),
            )
        )
        if len(boss_died_at) == 2:
            boss_died_at.append(0)

        if not (0 < len(boss_died_at) <= 3):
            print("Неправильный шаблон времени! (слишком много или мало элементов)")
            continue
        break

    boss_died_at = datetime(
        year=datetime.now().year,
        month=datetime.now().month,
        day=datetime.now().day,
        hour=boss_died_at[0],
        minute=boss_died_at[1],
        second=boss_died_at[2],
    )

    boss_respawn_after = timedelta(**bosses[selected_boss])
    print(
        f"\tБосс возродится через {boss_respawn_after} (h:m:s) в {(boss_died_at + boss_respawn_after).time()}!"
    )