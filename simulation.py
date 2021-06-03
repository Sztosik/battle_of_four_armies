import config
from army import Army
from board import Board
from jsonization import jsonization
import json
from visualization import main_visualization


class Simulation:
    def __init__(self):
        self.__armies = []
        self.__fraction_names = config.FRACTION_NAMES
        self.__board_x = 100
        self.__board_y = 100
        self.board = Board(self.__board_x, self.__board_y)

        new_army = Army("Lemon", 15, 7, 1, 1, self.board)
        self.__armies.append(new_army)
        new_army = Army("Green", 15, 7, 1, 99, self.board)
        self.__armies.append(new_army)
        new_army = Army("Blue", 15, 7, 99, 1, self.board)
        self.__armies.append(new_army)
        new_army = Army("Transparent", 15, 7, 99, 99, self.board)
        self.__armies.append(new_army)

    def start(self):
        """
        Rozpoczyna symulacje.
        """
        data = []
        single_itr_data = []
        for i in range(0, 1500):
            # oczywiście trzeba zmienić ten warunek, dodać info o zajętych polach i jednostkach do klasy armia
            print("\n\niteration number = %s" % i)
            for army in self.__armies:
                # print("\nARMY %s TURN" %army.fraction)
                army.start(self.board)
            # self.save_stats()
            single_itr_data.append(self.board.get_all_fields_data())
            data.append(jsonization(self.board, self.__board_x, self.__board_y))
        self.board.captured_fields()

        with open("sample.json", "w") as outfile:
            json.dump(data, outfile)

        path = 'sample.json'
        main_visualization(path)

    def save_stats(self):
        pass


if __name__ == "__main__":
    Symulacja = Simulation()
    Symulacja.start()
