from datetime import datetime, timedelta

bosses = {
    "арх": {"hours": 4, "minutes": 5},
    "звер": {"hours": 4, "minutes": 5},
    "декстр": {"hours": 5, "minutes": 5},
    "гт": {"hours": 5, "minutes": 5},
    "хюго": {"hours": 5, "minutes": 5},
    "бакс": {"hours": 5, "minutes": 5},
    "энт": {"hours": 1, "minutes": 28},
    "кк": {"hours": 2, "minutes": 5},
    "хозяин": {"hours": 5, "seconds": 5},
    "упырь_ворлакс": {"hours": 1, "minutes": 10},
    "упырь_лес_каталания": {"hours": 2, "seconds": 5},
    "остин": {"hours": 2, "seconds": 5},
    "альфа": {"hours": 2},
    "самка": {"hours": 2},
    "кт": {"hours": 2},
    "зт": {"hours": 2},
    "фарая": {"hours": 2},
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