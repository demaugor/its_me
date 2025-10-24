from tkinter import *

def choose(input):
    global state 
    state = input
    print(f"Selected: {state}")

root = Tk()

root.geometry("700x300")
root.title("Button")
root["bg"] = "red"

canvas = Canvas(root, width=400, height=320, bg="red")
canvas.grid(row=0, column=0, rowspan=7)

state = "circle"

# Создаем кнопки с разными функциями и размещаем их в разных ячейках
btn_square = Button(root, text="🟥", font=(None, 20), command=lambda: choose("square"))
btn_square.grid(row=0, column=1, padx=5, pady=5)

btn_line1 = Button(root, text="↘️", font=(None, 20), command=lambda: choose("Line1"))
btn_line1.grid(row=1, column=1, padx=5, pady=5)

btn_line2 = Button(root, text="↙️", font=(None, 20), command=lambda: choose("Line2"))
btn_line2.grid(row=2, column=1, padx=5, pady=5)

btn_plus = Button(root, text="➕", font=(None, 20), command=lambda: choose("plus"))
btn_plus.grid(row=3, column=1, padx=5, pady=5)

btn_minus = Button(root, text="➖", font=(None, 20), command=lambda: choose("minus"))
btn_minus.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()