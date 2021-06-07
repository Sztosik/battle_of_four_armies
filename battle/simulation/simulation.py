import json
import logging

import battle.simulation.config as config
from battle.army.army import Army
from battle.board.board import Board
from battle.visualization.jsonization import jsonization
from battle.visualization.visualization import main_visualization

logging.basicConfig(level=config.LOGGING_LEVEL)
logger = logging.getLogger(__name__)


class Simulation:
    """Główna klasa inicjująca i startująca symulacje."""

    def __init__(self):
        self.__armies: list[Army] = []
        self.__fraction_names: list[str] = config.FRACTION_NAMES
        self.__board_x: int = 100
        self.__board_y: int = 100
        self.board: Board = Board(self.__board_x, self.__board_y)

        new_army = Army("Red", 15, 7, config.POS_RED, self.board)
        self.__armies.append(new_army)
        new_army = Army("Green", 15, 7, config.POS_GREEN, self.board)
        self.__armies.append(new_army)
        new_army = Army("Blue", 15, 7, config.POS_BLUE, self.board)
        self.__armies.append(new_army)
        new_army = Army("Yellow", 15, 7, config.POS_YELLOW, self.board)
        self.__armies.append(new_army)

    def start(self):

        """Rozpoczyna symulacje."""
        data = []
        single_itr_data = []
        for i in range(0, 600):
            logger.info("iteration number = %s", i)

            for army in self.__armies:
                army.start(self.board)

            single_itr_data.append(self.board.get_all_fields_data())
            data.append(jsonization(self.board, self.__board_x, self.__board_y))
        logger.critical(self.board.captured_fields())

        with open("sample.json", "w") as outfile:
            json.dump(data, outfile)

        path = "sample.json"
        main_visualization(path, self.__board_x, self.__board_y)

    def save_stats(self):
        pass


if __name__ == "__main__":
    Symulacja = Simulation()
    Symulacja.start()
