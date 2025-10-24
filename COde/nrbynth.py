# Этот код рисует много прямоугольников (ярлыков) в окне.
# На каждом написано, как они "якобы" размещались бы с разными настройками pack: side, fill, expand.
# Мы используем сетку (grid) только чтобы красиво разложить их по таблице.
# Комментарии простые, чтобы ребёнок понял.

import tkinter as tk  # берём инструменты для создания окна

root = tk.Tk()                      # создаём главное окно
root.title("Пример side/fill/expand")  # заголовок окна
root.geometry("1200x800")           # размер окна: ширина 1200, высота 800

# Списки значений, которые будем показывать на блоках:
# expand: False (ложь) и True (правда)
expand_values = [False, True]
# fill: варианты заполнения (это параметры pack, мы просто показываем их текстом)
fill_values = [None, tk.X, tk.Y, tk.BOTH]
# side: стороны, куда "крепится" виджет в pack (верх, лево, низ, право)
side_values = [tk.TOP, tk.LEFT, tk.BOTTOM, tk.RIGHT]

# Пробежимся по всем комбинациям и создадим для каждой свой блок (Label)
for e, expand in enumerate(expand_values):
    for f, fill in enumerate(fill_values):
        for s, side in enumerate(side_values):
            # Мы используем grid, поэтому переводим side в букву для приклейки (sticky)
            # N — север (верх), S — юг (низ), W — запад (лево), E — восток (право)
            if side == tk.TOP:
                sticky = 'N'
            elif side == tk.BOTTOM:
                sticky = 'S'
            elif side == tk.LEFT:
                sticky = 'W'
            elif side == tk.RIGHT:
                sticky = 'E'
            else:
                sticky = ''

            # Текст, который увидим на блоке:
            # side — куда крепим, fill — как растягиваем, expand — расширяем ли свободное место
            text = f"side='{side}'\nfill='{fill}'\nexpand={expand}"

            # Цвет блока: красный, если expand=False; зелёный, если expand=True
            bg_color = '#55FF55' if expand else '#FF5555'

            # Создаём прямоугольник с текстом
            label = tk.Label(
                root,
                text=text,
                bg=bg_color,
                fg='black',
                relief='ridge',  # рамочка, чтобы блоки выделялись
                padx=8,
                pady=8
            )

            # Кладём блок в таблицу (grid)
            # row — строка, column — столбец
            # sticky — к какой стороне "приклеить" внутри своей ячейки
            # padx/pady — отступы вокруг блока
            label.grid(row=s + e * 4, column=f, sticky=sticky, padx=4, pady=4)

# Запускаем приложение — без этого окно не появится
root.mainloop()