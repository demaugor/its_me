import turtle

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("white")

# Настройка черепахи
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Рисуем большой круг (контур)
t.penup()
t.goto(0, -100)
t.setheading(90)
t.pendown()
t.pencolor("black")
t.circle(100)

# Черная половина
t.penup()
t.goto(0, -100)
t.setheading(90)
t.pendown()
t.fillcolor("#b04fb0")
t.begin_fill()
t.circle(100, 180)
t.circle(50, 180)
t.circle(-50, 180)
t.end_fill()

# Белая половина
t.penup()
t.goto(0, -100)
t.setheading(270)
t.pendown()
t.fillcolor("#ffffff")
t.begin_fill()
t.end_fill()

# Малый черный круг (в белой части)
t.penup()
t.goto(-70, -100)  # Центр белой половины
t.pendown()
t.pencolor("black")
t.fillcolor("#b04fb0")
t.begin_fill()
t.circle(20)
t.end_fill()

# Малый белый круг (в черной части)
t.penup()
t.goto(-170, -100)  # Центр черной половины
t.pendown()
t.pencolor("black")
t.fillcolor("#b5d2ee")
t.begin_fill()
t.circle(20)
t.end_fill()

# Подпись
t.penup()
t.goto(-100, -230)
t.pendown()
t.pencolor("black")
t.pensize(1)
t.write("Мориц Данила", font=("Arial", 20, "bold"))

t.hideturtle()
turtle.done()