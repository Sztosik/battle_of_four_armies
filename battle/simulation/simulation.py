import copy
import logging
import sys
import threading
import time
from queue import Queue

import battle.simulation.config as config
from battle.army.army import Army
from battle.board.board import Board
from battle.visualization.visualization import main_visualization

logging.basicConfig(level=config.LOGGING_LEVEL)
logger = logging.getLogger(__name__)


class Simulation:
    """Główna klasa inicjująca i startująca symulacje."""

    def __init__(self):
        self.__armies: list[Army] = []
        self.__fraction_names: list[str] = config.FRACTION_NAMES
        self.__board_x: int = 50
        self.__board_y: int = 50
        self.board: Board = Board(self.__board_x, self.__board_y)
        self.__end_condition = 0.5

        new_army = Army("Red", 0, 80, config.POS_RED, self.board)
        self.__armies.append(new_army)
        new_army = Army("Green", 80, 7, config.POS_GREEN, self.board)
        self.__armies.append(new_army)
        new_army = Army("Blue", 80, 7, config.POS_BLUE, self.board)
        self.__armies.append(new_army)
        new_army = Army("Yellow", 80, 7, config.POS_YELLOW, self.board)
        self.__armies.append(new_army)

    def sim_thread(self, board_state: Queue):
        """Rozpoczyna symulacje."""

        iteration = 0
        while True:
            iteration += 1
            logger.info("iteration number = %s", iteration)

            for army in self.__armies:
                army.start(self.board)

            current_board_state = copy.copy(self.board)
            board_state.put(current_board_state)
            time.sleep(config.SINGLE_FRAME_DURATION / 1000)

            iteration_stats = self.board.captured_fields()
            maximum = max(iteration_stats.values())
            percentage_of_captured_fields = maximum / (self.__board_x * self.__board_y)
            logger.critical(iteration_stats)
            
            if percentage_of_captured_fields > self.__end_condition:
                winner = max(iteration_stats, key=iteration_stats.get)
                logger.critical(f"ITERATION: {iteration} WINNER: {winner}")
                break
        sys.exit()

    def run(self):
        board_state = Queue()

        simulation_thread = threading.Thread(
            target=self.sim_thread, args=(board_state,)
        )
        visualization_thread = threading.Thread(
            target=main_visualization,
            args=(board_state, self.__board_x, self.__board_y),
        )

        simulation_thread.start()
        visualization_thread.start()

        board_state.join()
        simulation_thread.join()
        visualization_thread.join()

    def save_stats(self):
        pass


if __name__ == "__main__":
    Symulacja = Simulation()
    Symulacja.run()
