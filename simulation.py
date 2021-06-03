import config
from army import Army
from board import Board


class Simulation:
    def __init__(self):
        self.__armies = []
        self.__fraction_names = config.FRACTION_NAMES
        self.__board_x = 100
        self.__board_y = 100
        self.board = Board(self.__board_x, self.__board_y)

        new_army = Army("Lemon", 3, 3, 1, 1, self.board)
        self.__armies.append(new_army)
        new_army = Army("Green", 3, 3, 1, 99, self.board)
        self.__armies.append(new_army)
        new_army = Army("Blue", 3, 3, 99, 1, self.board)
        self.__armies.append(new_army)
        new_army = Army("Transparent", 3, 3, 99, 99, self.board)
        self.__armies.append(new_army)

    def start(self):
        """
        Rozpoczyna symulacje.
        """
        for i in range(0, 1500):
            print(i)
            # oczywiście trzeba zmienić ten warunek, dodać info o zajętych polach i jednostkach do klasy armia
            print("\n\niteration number = %s" % i)
            for army in self.__armies:
                # print("\nARMY %s TURN" %army.fraction)
                army.start(self.board)
            # self.save_stats()
        self.board.captured_fields()

    def save_stats():
        pass


if __name__ == "__main__":
    Symulacja = Simulation()
    Symulacja.start()
