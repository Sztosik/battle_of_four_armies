import copy
import json
import logging
import sys
import time
from queue import Queue

import battle.simulation.config as config
from battle.army.army import Army
from battle.board.board import Board
from battle.simulation.stats import Stast


logging.basicConfig(level=config.LOGGING_LEVEL)
logger = logging.getLogger(__name__)


class Simulation:
    """Główna klasa inicjująca i startująca symulacje."""

    def __init__(self, json_path="init_data.json"):
        with open(json_path, "r") as f:
            init_data = json.load(f)

            self.__armies: list[Army] = []
            self.__board_x: int = init_data["board_x"]
            self.__board_y: int = init_data["board_y"]
            self.__end_condition = init_data["percentage"]
            self.board: Board = Board(self.__board_x, self.__board_y)
            self.stats = Stast()

            config.SINGLE_FRAME_DURATION = init_data["delay"]

            new_army = Army("Red", init_data["red_base_units"], init_data["red_special_units"], config.POS_RED, self.board)
            self.__armies.append(new_army)

            new_army = Army("Green", init_data["green_base_units"], init_data["green_special_units"], config.POS_GREEN, self.board)
            self.__armies.append(new_army)

            new_army = Army("Blue", init_data["blue_base_units"], init_data["blue_special_units"], config.POS_BLUE, self.board)
            self.__armies.append(new_army)

            new_army = Army("Yellow", init_data["yellow_base_units"], init_data["yellow_special_units"], config.POS_YELLOW, self.board)
            self.__armies.append(new_army)


    def send_data(self, units_stats):
        """Przekazuje dane do ststystyk."""

        iteration_stats = self.board.captured_fields()
        self.stats.add_row(iteration_stats, units_stats)


    def sim_end(self) -> bool:
        """"Sprawdza czy został spełniony warunek końca symulacji."""

        iteration_stats = self.board.captured_fields()
        maximum = max(iteration_stats.values())
        percentage_of_captured_fields = (
            maximum / (self.__board_x * self.__board_y)
        ) * 100

        if percentage_of_captured_fields > self.__end_condition:
            winner = {
                key for key, value in iteration_stats.items() if value == maximum
            }
            logger.critical(f"WINNER: {winner}")
            return True
        return False


    def sim_thread(self, board_state: Queue):
        """Rozpoczyna symulacje."""

        iteration = 0
        while True:
            iteration += 1
            logger.debug("iteration number = %s", iteration)

            units_stats: dict = dict()

            for army in self.__armies:
                army.start(self.board)
                units_stats[army.fraction] = army.count_units()

            self.send_data(units_stats)

            current_board_state = copy.copy(self.board)
            board_state.put(current_board_state)

            if self.sim_end():
                self.board.end = True
                current_board_state = copy.copy(self.board)
                board_state.put(current_board_state)
                self.stats.save_to_csv()
                break

            time.sleep(config.SINGLE_FRAME_DURATION / 1000)

        sys.exit()



if __name__ == "__main__":
    pass
