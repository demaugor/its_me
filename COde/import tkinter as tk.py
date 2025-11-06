import tkinter as tk
import random

def setup_game():
    global correct_button
    # Удаляем все кнопки перед началом новой игры
    for btn in buttons:
        btn.destroy()
    buttons.clear()

    # Создаем 4 кнопки
    for i in range(4):
        btn = tk.Button(root, text=f"Кнопка {i+1}", width=15, height=2)
        btn.pack(side='left', padx=10, pady=10)
        buttons.append(btn)

    # Выбираем случайную кнопку правильной
    correct_button = random.choice(buttons)
    correct_button.config(command=correct_guess)

    # Для остальных кнопок задаем неправильный обработчик
    for btn in buttons:
        if btn != correct_button:
            btn.config(command=wrong_guess)

def correct_guess():
    label.config(text="Ты угадал!")

def wrong_guess():
    # Удаляем все неправильные кнопки
    for btn in buttons[:]:
        if btn != correct_button:
            btn.destroy()
            buttons.remove(btn)
    label.config(text="Ты не угадал >:(")

root = tk.Tk()
root.title("Игра: Выбери правильную кнопку")

buttons = []

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=10)

#frame = tk.Frame(root)
#frame.pack()

# Инициализация игры
setup_game()

# Кнопка перезапуска игры (опционально)
restart_button = tk.Button(root, text="Заново", command=setup_game)
restart_button.pack(pady=10)

root.mainloop()