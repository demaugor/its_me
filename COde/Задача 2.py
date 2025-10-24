import tkinter as tk
import math

class ShadowedRect:
    def __init__(self, canvas: tk.Canvas, x, y, width, height, shadow_offset=10, shadow_angle_deg=15, color="skyblue", shadow_color="gray"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shadow_offset = shadow_offset
        self.shadow_angle = math.radians(shadow_angle_deg)
        self.color = color
        self.shadow_color = shadow_color

        self.shadow_id = None
        self.rect_id = None

        self.draw()

    def draw(self):
        # Удалить старые
        if self.shadow_id is not None:
            self.canvas.delete(self.shadow_id)
        if self.rect_id is not None:
            self.canvas.delete(self.rect_id)

        # Вычислить смещение тени
        dx = self.shadow_offset * math.cos(self.shadow_angle)
        dy = self.shadow_offset * math.sin(self.shadow_angle)

        # Тень как полигон
        pts = [
            self.x + dx,              self.y + dy,
            self.x + dx + self.width, self.y + dy,
            self.x + dx + self.width, self.y + dy + self.height,
            self.x + dx,              self.y + dy + self.height
        ]
        self.shadow_id = self.canvas.create_polygon(pts, fill=self.shadow_color, outline="")

        # Прямоугольник над тенью
        self.rect_id = self.canvas.create_rectangle(self.x, self.y,
                                                    self.x + self.width, self.y + self.height,
                                                    fill=self.color, outline="black")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.draw()

def main():
    root = tk.Tk()
    root.title("Движение с тенью")

    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    sr = ShadowedRect(canvas, x=200, y=150, width=120, height=80,
                      shadow_offset=15, shadow_angle_deg=20,
                      color="skyblue", shadow_color="gray70")

    def on_key(event):
        # event.keysym — имя клавиши
        key = event.keysym.lower()
        step = 10
        if key == 'w':
            sr.move(0, -step)
        elif key == 's':
            sr.move(0, step)
        elif key == 'a':
            sr.move(-step, 0)
        elif key == 'd':
            sr.move(step, 0)

    # Привязки к root
    root.bind("<KeyPress>", on_key)

    # Важно: установить фокус, чтобы root получал события клавиатуры
    root.focus_set()

    root.mainloop()

if __name__ == "__main__":
    main()
