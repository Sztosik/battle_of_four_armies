import copy
import json
import logging
import sys
import threading
import time
from queue import Queue

import battle.simulation.config as config
from battle.army.army import Army
from battle.board.board import Board
from battle.simulation.stats import Stast
from battle.visualization.visualization import main_visualization

logging.basicConfig(level=config.LOGGING_LEVEL)
logger = logging.getLogger(__name__)


class Simulation:
    """Główna klasa inicjująca i startująca symulacje."""

    def __init__(self, json_path = "init_data.json"):
        with open(json_path, 'r') as f:
            init_data = json.load(f)

            self.__armies: list[Army] = []
            self.__board_x: int = init_data['board_x']
            self.__board_y: int = init_data['board_y']
            self.__end_condition = 0.6
            self.board: Board = Board(self.__board_x, self.__board_y)
            self.stats = Stast()
            # init_data[]
            new_army = Army(
                "Red",
                init_data['red_base_units'],
                init_data['red_special_units'],
                config.POS_RED,
                self.board
            )
            self.__armies.append(new_army)

            new_army = Army(
                "Green",
                init_data['green_base_units'],
                init_data['green_special_units'],
                config.POS_GREEN,
                self.board
            )
            self.__armies.append(new_army)

            new_army = Army(
                "Blue", 
                init_data['blue_base_units'], 
                init_data['blue_special_units'], 
                config.POS_BLUE, 
                self.board
            )
            self.__armies.append(new_army)

            new_army = Army(
                "Yellow", 
                init_data['yellow_base_units'], 
                init_data['yellow_special_units'], 
                config.POS_YELLOW, 
                self.board)
            self.__armies.append(new_army)

    def sim_thread(self, board_state: Queue):
        """Rozpoczyna symulacje."""

        iteration = 0
        while True:
            iteration += 1
            logger.info("iteration number = %s", iteration)
            
            units_stats: dict = dict()

            for army in self.__armies:
                army.start(self.board)
                units_stats[army.fraction] = army.count_units()

            current_board_state = copy.copy(self.board)
            board_state.put(current_board_state)
            time.sleep(config.SINGLE_FRAME_DURATION / 1000)

            iteration_stats = self.board.captured_fields()
            self.stats.add_row(iteration_stats, units_stats)
            maximum = max(iteration_stats.values())
            percentage_of_captured_fields = maximum / (self.__board_x * self.__board_y)
            logger.critical(iteration_stats)

            if percentage_of_captured_fields > self.__end_condition:
                winner = max(iteration_stats, key=iteration_stats.get)
                logger.critical(f"ITERATION: {iteration} WINNER: {winner}")
                self.stats.save_to_csv()
                break
        sys.exit()

    def run(self):
        board_state = Queue()

        simulation_thread = threading.Thread(
            target=self.sim_thread, args=(board_state,)
        )
        visualization_thread = threading.Thread(
            target=main_visualization,
            args=(board_state, self.__board_x, self.__board_y)
        )

        simulation_thread.start()
        visualization_thread.start()

        board_state.join()
        simulation_thread.join()
        visualization_thread.join()


if __name__ == "__main__":
    Symulacja = Simulation()
    Symulacja.run()
    sys.exit()