import tkinter as tk
from tkinter import Button, Canvas, Entry, Frame, Label, Toplevel, scrolledtext
from tkinter.constants import CENTER, END, RIGHT, TOP

from PIL import Image, ImageTk
import pandas as pd

class ViewGame:
    def __init__(self, controller, res_path):
        self.show_country = False
        self.which_country = False
        self.res_path = res_path
        self.csvfile = pd.read_csv(res_path["csv"])
        self.__show_window()
        self.__make_markup()
        img = ImageTk.PhotoImage(Image.open(res_path["img"]).resize((1300, 740), Image.ANTIALIAS))
        self.game_field.create_image(640, 360, anchor=CENTER, image=img)
        self.__place_buttons(len(self.csvfile['country']))
        self.__place_numbers(res_path["csv"])
        self.__place_action_buttons(controller)
        self.game_window.mainloop()

    def pop_answer(self):
        answer = self.answer_box.get()
        self.__clear_answer_box()
        return answer

    def __place_map(self, res_path):
        pilimage = Image.open(res_path["img"])
        img = ImageTk.PhotoImage(pilimage.resize((1300, 740), Image.ANTIALIAS))
        self.x = self.game_field.create_image(640, 360, anchor=CENTER, image=img)

    def __show_window(self):
        self.game_window = Toplevel()
        self.game_window.title("Мировое господство")
        self.game_window.geometry('1920x1080')

    def close_window(self):
        self.game_window.destroy()

    def __make_markup(self):
        self.game_field = Canvas(self.game_window, width=1280, height=720)
        self.buttons_frame = Frame(self.game_window)
        self.action_frame = Frame(self.game_window)

        self.game_field.pack(side=RIGHT)
        self.buttons_frame.pack()
        self.action_frame.pack()

    def __place_action_buttons(self, controller):
        Button(self.action_frame, text="Отгадывать любую страну", command=lambda: controller.which_one_country()).grid(column=0, row=0)
        Button(self.action_frame, text="Включить режим обучения", command=lambda: controller.set_tutorial()).grid(
            column=0, row=1)
        Button(self.action_frame, text="Показывать страны, которые нужно отгадать",
               command=lambda: controller.show_guess(self)).grid(column=0, row=2)
        Button(self.action_frame, text="Помощь", command=self.__open_help).grid(column=0, row=3)

        self.__text_field = scrolledtext.ScrolledText(self.action_frame, width=30, height=10)
        self.__text_field.grid(column=0, row=5)
        Button(self.action_frame, text="Cancel", command=lambda: controller.goto_main_screen(self)).grid(column=0,
                                                                                                         row=6)
        Label(self.action_frame, text="Введите название:").grid(column=0, row=7)
        self.answer_box = Entry(self.action_frame, width=20)
        self.answer_box.grid(column=0, row=8)
        Button(self.action_frame, text="Отправить", command=lambda: controller.check(self)).grid(column=0, row=9)
        self.answer_box.focus()

    def __clear_answer_box(self):
        self.answer_box.delete(0, END)

    def __open_help(self):
        help_window = Toplevel()
        help_window.title("Мировое господство")
        help_window.geometry('580x640')
        font_style = "Arial Bold"

        font_size_heading = 30
        font_size_subtitle = 14
        font_size_desc = 11
        font_size_subdesc = 9
        text = []
        text.append(Label(help_window, text="Описание игры", font=(font_style, font_size_heading)))
        text.append(Label(help_window, text="Игра предназначена для обучения. Целью игры является ",
                          font=(font_style, font_size_desc)))
        text.append(Label(help_window, text="запоминание расположения и названий всех стран/городов мира.",
                          font=(font_style, font_size_desc)))
        text.append(Label(help_window, text="Вводите название страны в поле и проверяйте свои знания!",
                          font=(font_style, font_size_desc)))
        text.append(Label(help_window, text="Описание режимов", font=(font_style, font_size_heading)))
        text.append(Label(help_window, text="-Отгадывать любую страну", font=(font_style, font_size_subtitle)))
        text.append(Label(help_window, text="В поле ответа можно вводить название любой страны",
                          font=(font_style, font_size_subdesc)))
        text.append(Label(help_window, text="-Отгадывать определенную страну", font=(font_style, font_size_subtitle)))
        text.append(Label(help_window, text="Перед тем как вводить свой ответ, нажмите на номер страны, которую хотите "
                                            "отгадать", font=(font_style, font_size_subdesc)))
        text.append(Label(help_window, text="-Включить режим обучения", font=(font_style, font_size_subtitle)))
        text.append(
            Label(help_window, text="В поле ответа можно вводить цифры, которые будут открывать неизвестные страны",
                  font=(font_style, font_size_subdesc)))
        text.append(Label(help_window, text="-Выключить режим обучения", font=(font_style, font_size_subtitle)))
        text.append(
            Label(help_window, text="Отключает функционал режима обучения", font=(font_style, font_size_subdesc)))
        text.append(Label(help_window, text="-Показывать страны, которые нужно отгадать",
                          font=(font_style, font_size_subtitle)))
        text.append(Label(help_window, text="Отображает список стран, которые ещё не угаданы",
                          font=(font_style, font_size_subdesc)))
        text.append(
            Label(help_window, text="-Скрыть страны, которые нужно отгадать", font=(font_style, font_size_subtitle)))
        text.append(Label(help_window, text="Скрывает список стран, которые ещё не угаданы",
                          font=(font_style, font_size_subdesc)))
        for i in range(len(text)):
            text[i].pack(side=TOP)
        help_window.mainloop()

    def __place_buttons(self, num_of_countries, max_buttons_in_row=5):
        col, row = 1, 1
        for i in range(num_of_countries):
            Button(self.buttons_frame, text=i + 1, command=lambda: self.set_target(i)).grid(column=col, row=row)
            if (i + 1) % max_buttons_in_row == 0:
                row += 1
                col = 1
            else:
                col += 1

    def __place_numbers(self, csv_path, font_style="Arial Bold", color="red"):
        self.numbers_dict = dict()
        csv_dataframe = pd.read_csv(csv_path)
        num_of_countries = len(csv_dataframe['country'])
        for i in range(num_of_countries):
            x = csv_dataframe['x'][i]
            y = csv_dataframe['y'][i]
            size = csv_dataframe['size'][i]
            tmp = self.game_field.create_text(x, y, text=i + 1, font=(font_style, size), fill=color)
            self.numbers_dict[csv_dataframe['country'][i]] = tmp
            print(self.numbers_dict)

    def replace_text(self, answer):
        if answer.isdigit():
            i = self.csvfile["country"].tolist().index(self.csvfile["country"].tolist()[int(answer)])
        else:
            i = self.csvfile["country"].tolist().index(answer)
        x = self.csvfile['x'][i]
        y = self.csvfile['y'][i]
        x = self.csvfile['x'][i]
        y = self.csvfile['y'][i]
        size = self.csvfile['size'][i]
        font_style = "Arial Bold"
        color = "red"
        if answer.isdigit():
            answer = int(answer) + 1
            print(answer, self.numbers_dict)
            number = self.numbers_dict.pop(self.numbers_dict.get(i))
        else:
            number = self.numbers_dict.pop(answer)
        try:
            self.game_field.delete(number)
            self.game_field.create_text(x, y, text=answer, font=(font_style, size), fill=color)
        except KeyError:
            pass

    def set_win(self):
        self.__text_field.delete('1.0', END)
        self.__text_field.insert(tk.INSERT, "win")

    def print_guess(self, states):
        if not self.show_country:
            print(states)
            self.__text_field.delete('1.0', END)
            i = 1
            for state in states:
                self.__text_field.insert("1.0", state + '\n')
                i += 1
            self.show_country = True
        else:
            self.__text_field.delete('1.0', END)
            self.show_country = False

    def set_target(self, number):
        pass
