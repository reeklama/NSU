from tkinter import Canvas, Image, Tk, Label, Button
from tkinter.constants import CENTER, RIGHT
from PIL import Image, ImageTk

class ViewMenu:
    def __init__(self, controller):
        self.window = Tk()
        window = self.window
        window.title("Мировое господство")
        window.geometry('1920x1080')
        Label(window, text="Мировое господство", font=("Arial Bold", 40)).grid(column=4, row=0)
        Button(window, text="Австралия", command=lambda: controller.start_game(self,1)).grid(column=4, row=1)
        Button(window, text="Африка", command=lambda: controller.start_game(self,2)).grid(column=4, row=2)
        Button(window, text="Евразия", command=lambda: controller.start_game(self,3)).grid(column=4, row=3)
        Button(window, text="Северная Америка", command=lambda: controller.start_game(self,4)).grid(column=4, row=4)
        Button(window, text="Южная Америка", command=lambda: controller.start_game(self,5)).grid(column=4, row=5)
        window.mainloop()

    def hide_window(self):
        self.window.withdraw()

    def show_window(self):
        self.window.deiconify()

    def get_window(self):
        return self.window