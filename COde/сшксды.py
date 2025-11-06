from tkinter import *
import time

root = Tk()
root.geometry("800x600")
root.title("Анимация")
root["bg"] = 'white'
canvas = Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Создаем два шарика
hero = canvas.create_oval(80, 80, 120, 120, fill="red")
hero2 = canvas.create_oval(200, 200, 240, 240, fill="blue")

# Скорости для первого шарика (красного)
h_x = 3
h_y = 2

# Скорости для второго шарика (синего)
h2_x = -2
h2_y = -3

def draw():
    global h_x, h_y, h2_x, h2_y
    
    # Движение первого шарика (красного)
    x1, y1, x2, y2 = canvas.coords(hero)
    
    # Проверка столкновений для первого шарика
    if x1 <= 0 or x2 >= 800:  # левая или правая стенка
        h_x = -h_x
    if y1 <= 0 or y2 >= 600:  # верхняя или нижняя стенка
        h_y = -h_y
    
    # Движение второго шарика (синего)
    dx1, dy1, dx2, dy2 = canvas.coords(hero2)
    
    # Проверка столкновений для второго шарика
    if dx1 <= 0 or dx2 >= 800:  # левая или правая стенка
        h2_x = -h2_x
    if dy1 <= 0 or dy2 >= 600:  # верхняя или нижняя стенка
        h2_y = -h2_y
    
    # Перемещаем оба шарика
    canvas.move(hero, h_x, h_y)
    canvas.move(hero2, h2_x, h2_y)

# Используем after для анимации вместо while True
def animate():
    draw()
    root.after(10, animate)  # вызываем себя каждые 10ms

# Запускаем анимацию
animate()

root.mainloop()