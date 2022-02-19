from viewMenu import ViewMenu
from gameController import GameController

class MenuController:
    def __init__(self):
        ViewMenu(self)
        
    def start_game(self, view, map_id):
        res_path = self.choose_map(map_id)
        view.hide_window()
        GameController(view.get_window(), res_path)
        print(1)

    def choose_map(self, map_id):
        if map_id == 1:
            return {"img":"resources/Австралия.jpg", "csv":"resources/data_country_Australia.csv"}
        elif map_id == 2:
            return {"img":"resources/Африка.jpg", "csv":"resources/data_country_Afrika.csv"}
        elif map_id == 3:
            return {"img":"resources/Евразия.jpg", "csv":"resources/data_country_EA.csv"}
        elif map_id == 4:
            return {"img":"resources/СевернаяАмерика.jpg", "csv":"resources/data_country_NA.csv"}
        elif map_id == 5:
            return {"img":"resources/ЮжнаяАмерика.jpg", "csv":"resources/data_country_SA.csv"}
            