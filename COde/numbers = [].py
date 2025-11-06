import turtle

# Настройка экрана
screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Спираль")

# Создание черепахи
t = turtle.Pen()
t.speed(0)  # Максимальная скорость

colors = ["red", "green", "orange", "blue"]
name = turtle.textinput('Введите свое имя', 'Как тебя зовут?')

# Поднимаем перо перед началом движения
t.up()

for x in range(100):
    t.pencolor(colors[x % 4])
    
    # Опускаем перо, пишем имя, поднимаем перо
    t.down()
    t.write(name, font=("Arial", int((x+4)//4), "normal"))
    t.up()
    
    # Двигаемся вперед
    t.forward(x * 4)
    t.left(91)

# Завершение программы
turtle.mainloop()