import config
from army import Army
from board import Board

# zrobić wybór czy chce się wpisywać parametry początkowe czy wystartować z domyślnych
class Simulation: 

    board = []

    def __init__(self):
        self.__armies = []
        self.__fraction_names = config.FRACTION_NAMES
        self.__board_x = input("type x: ")
        self.__board_y = input("type y: ")

        board = Board(self.__board_x, self.__board_y)

        for army in self.__fraction_names:
            init_number_of_base_units = input("podaj liczbę jednostek podstawowych: ")
            init_number_of_special_units = input("podaj liczbę jednostek specjalnych: ")
            start_point_x = input("start point - type x: ")
            start_point_y = input("start point - type y: ")
            new_army = Army(army, init_number_of_base_units, init_number_of_special_units, start_point_x, start_point_y)
            self.__armies.append(new_army)

    def start(self):
        while True: # oczywiście trzeba zmienić ten warunek, dodać info o zajętych polach i jednostkach do klasy armia
            for army in self.__armies:
                army.start()
            self.save_stats()

    def save_stats():
        pass