from numpy import fabs
import pandas as pd


class Gamemode:
    normal = False
    tutorial = False
    byNumbers = False
    target = -1

    def __init__(self):
        self.set_normal()

    def set_normal(self):
        self.normal = True
        self.tutorial = False
        self.byNumbers = False

    def set_tutorial(self):
        self.normal = False
        self.tutorial = True
        self.byNumbers = False

    def set_bynumbers(self, target):
        self.normal = False
        self.tutorial = False
        self.byNumbers = True
        self.target = target


class Model:

    def __init__(self, csv_path):
        self.csv_dataframe = pd.read_csv(csv_path)
        self.remain_states = self.csv_dataframe['country'].tolist()
        self.num_of_countries = len(self.remain_states)
        self.guessed_states = []
        self.gamemode = Gamemode()
        self.set_gamemode(self.gamemode, 2)
        self.normal = True
        self.tutorial = False

    def set_gamemode(self, gm, target=-1):
        if (gm == 1):
            self.gamemode.set_normal()
        elif (gm == 2):
            self.gamemode.set_tutorial()
        elif (gm == 3):
            self.gamemode.set_bynumbers(target)

    def get_guess(self):
        return self.remain_states

    def set_which(self):
        if not self.byNumbers:
            self.byNumbers = True
        else:
            self.byNumbers = False


    def set_tutorial(self):
        self.tutorial = True
        self.normal = False

    def set_normal(self):
        self.tutorial = False
        self.normal = True

    def check(self, answer):
        if answer == "exit":
            new_data = pd.DataFrame(self.remain_states)
            new_data.to_csv("states_to_learn.csv")
            print(self.remain_states)
            print("exit")
            return self.remain_states

        if self.normal == True:
            print("normal")
            if answer in self.remain_states:
                self.guessed_states.append(answer)
                self.remain_states.pop(self.remain_states.index(answer))
                if len(self.guessed_states) == self.num_of_countries:
                    print("WIN")
                    win = 5
                    return win
                return True
            else:
                return False
        elif self.tutorial == True:
            print("tutorial")
            if answer.isdigit() and int(answer) > 0 and int(answer) < self.num_of_countries:
                print(self.guessed_states)
                print(self.remain_states)
                state = self.remain_states[int(answer)]
                self.guessed_states.append(state)
                self.remain_states.pop(self.remain_states.index(state))

                if len(self.guessed_states) == self.num_of_countries:
                    win = 5
                    return win
                return state
            return False
