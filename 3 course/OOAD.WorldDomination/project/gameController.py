import pandas as pd
from model import Model
from viewGame import ViewGame


class GameController:
    def __init__(self, main_window, res_path):
        self.__main_window = main_window
        self.__model = Model(res_path["csv"])
        self.__csv_dataframe = pd.read_csv(res_path['csv'])
        ViewGame(self, res_path)

    def goto_main_screen(self, view):
        view.close_window()
        self.__main_window.deiconify()

    def check(self, view):
        answer = view.pop_answer()
        status = self.__model.check(answer)
        print(status, status == 5, type(status))
        if status == True:
            view.replace_text(answer)
        if status == 5:
            view.replace_text(answer)
            view.set_win()
        elif status != False:
            view.print_guess(status)

    def which_one_country(self):
        print()

    def show_guess(self, view):
        view.print_guess(self.__model.get_guess())

    def set_tutorial(self):
        self.__model.set_tutorial()
