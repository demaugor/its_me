from tkinter import *
from tkinter.colorchooser import *

# Создаём глобальную переменную для хранения текущего выбора
def choise(input):
    global state
    global xfgh
    if input == 'plus' and xfgh < 98:
        xfgh += 2
        status_label.configure(text= xfgh)
        return
    elif input == 'minus' and xfgh > 0:
        xfgh -= 2
        status_label.configure(text= xfgh)
        return
    state = input

# Создаём окно и настройки
root = Tk()
root.geometry("600x400")
root.title("рисовалка")
root["bg"] = 'gray75'

# Создаём холст
ghost = Canvas(root, width= 540, height= 400, bg = "white")
ghost.grid(row= 0, column= 0, rowspan= 7)

# Объявляем переменную для размера фигур
xfgh = 10
# Цвет выбранный для рисования
zjhe = 'green'

# Создаём кнопку для выбора квадрата
Button1 = Button(root, text='🟥', font= (None, 20), command= lambda:choise('square'))
Button1.grid(row= 0, column= 1)

# Кнопка для выбора круга
Button2 = Button(root, text='🔴', font= (None, 20), command= lambda:choise('circle'))
Button2.grid(row= 1, column= 1)

# Кнопка для линии 1
Button3 = Button(root, text='↘️', font= (None, 20), command= lambda:choise('line1'))
Button3.grid(row= 2, column= 1)

# Кнопка для линии 2
Button4 = Button(root, text='↙️', font= (None, 20), command= lambda:choise('line2'))
Button4.grid(row= 3, column= 1)

# Кнопка для плюса
Button5 = Button(root, text='➕', font= (None, 20), command= lambda:choise('plus'))
Button5.grid(row= 4, column= 1)

# Кнопка для минуса
Button6 = Button(root, text='➖', font= (None, 20), command= lambda:choise('minus'))
Button6.grid(row= 5, column= 1)

# Метка, показывающая текущий статус
status_label = Label(root, text=xfgh, fg=zjhe, font= (None,32))
status_label.grid(row= 6, column= 1)

# Изначально выбран инструмент
global state
state = 'square'  # можно задать по умолчанию

# Обработчик щелчка по холсту
def paint(event):
    if event.widget.__class__ is not Canvas:  # Исправлено: .class на .__class__
        return
    global xfgh, zjhe
    if state == 'circle':
        ghost.create_oval(event.x - xfgh,
                          event.y - xfgh,
                          event.x + xfgh,
                          event.y + xfgh,
                          fill= zjhe,
                          outline= zjhe)
    elif state == 'square':
        ghost.create_rectangle(event.x - xfgh,
                               event.y - xfgh,
                               event.x + xfgh,
                               event.y + xfgh,
                               fill= zjhe,
                               outline= zjhe)
    elif state == 'line1':
        ghost.create_line(event.x - xfgh,
                          event.y - xfgh,
                          event.x + xfgh,
                          event.y + xfgh,
                          fill= zjhe,
                          width=2)
    elif state == 'line2':
        ghost.create_line(event.x - xfgh,
                          event.y + xfgh,
                          event.x + xfgh,
                          event.y - xfgh,
                          fill= zjhe,
                          width=2)

# Привязываем обработчик к клику
root.bind('<Button-1>', paint)
root.bind('<B1-Motion>', paint)

def eraser(event):
    ghost.create_oval(event.x - xfgh * 2, event.y - xfgh * 10,
                      event.x + xfgh * 2, event.y + xfgh * 10,
                      fill="white", outline="white")
    
root.bind('<3>', eraser)
root.bind('<B3-Motion>', eraser)

def ask_color(event):
    global zjhe
    color_code = askcolor(title= 'выберите цвет')
    zjhe = color_code[1]
    status_label.configure(fg= zjhe)

def ochistka(event=None):  # Добавлен параметр event для работы с bind
    ghost.delete("all")  # Исправлено: Canvas.delete на ghost.delete

# Добавляем кнопку для очистки
clear_button = Button(root, text='Очистить', font= (None, 12), command=ochistka)
clear_button.grid(row= 7, column= 1)

root.bind('<BackSpace>', ochistka)  # Исправлено: Backspace на BackSpace

ghost.bind('<Button-2>', ask_color)  # Исправлено: <2> на <Button-2>
root.mainloop()