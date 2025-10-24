import tkinter as tk

class MovingButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Движущаяся кнопка с тенью")
        
        self.canvas = tk.Canvas(root, width=400, height=200)
        self.canvas.pack()

        # Создаем тень
        self.shadow_offset = 5
        self.button_x = 150
        self.button_y = 80

        # Создаем тень
        self.shadow = self.canvas.create_rectangle(
            self.button_x + self.shadow_offset,
            self.button_y + self.shadow_offset,
            self.button_x + 100 + self.shadow_offset,
            self.button_y + 30 + self.shadow_offset,
            fill='gray'
        )

        # Создаем кнопку
        self.button = self.canvas.create_rectangle(
            self.button_x,
            self.button_y,
            self.button_x + 100,
            self.button_y + 30,
            fill='blue'
        )

        # Текст на кнопке
        self.text = self.canvas.create_text(
            self.button_x + 50,
            self.button_y + 15,
            text='Кнопка',
            fill='white'
        )

        # Создаем кнопки управления
        self.btn_left = tk.Button(root, text="Влево", command=self.move_left)
        self.btn_left.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_right = tk.Button(root, text="Вправо", command=self.move_right)
        self.btn_right.pack(side=tk.RIGHT, padx=10, pady=10)

    def move_left(self):
        self.move_button(-10)

    def move_right(self):
        self.move_button(10)

    def move_button(self, delta_x):
        # Обновляем позицию
        self.canvas.move(self.shadow, delta_x, 0)
        self.canvas.move(self.button, delta_x, 0)
        self.canvas.move(self.text, delta_x, 0)

root = tk.Tk()
app = MovingButtonApp(root)
root.mainloop()