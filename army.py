from board import Board
from unit import BaseUnit


class Army:
    """Przechowuje jednostki i zbiera ich statystyki."""
    def __init__(
        self,
        fraction,
        init_number_of_base_units,
        init_number_of_special_units,
        start_point_x,
        start_point_y,
        board,
    ):
        self.fraction = fraction
        self.__init_number_of_base_units = init_number_of_base_units
        self.__init_number_of_special_units = init_number_of_special_units
        self.__unit_list = []
        self.__start_point_x = start_point_x
        self.__start_point_y = start_point_y

        self.generate_unit_list(board)

    def generate_unit_list(self, board: Board) -> None:
        """
        Tworzy obiekty jednostek należących do armii i dodaje je do listy
        """
        for _ in range(self.__init_number_of_base_units):
            new_unit = BaseUnit(
                self.fraction, self.__start_point_x, self.__start_point_y, board
            )
            self.__unit_list.append(new_unit)

        # for id in range(self.__init_number_of_special_units):
        #     new_unit = BaseUnit(id, self.fraction, self.__start_point_x, self.__start_point_y)
        #     self.__unit_list.append(new_unit)

    def start(self, board: Board) -> None:
        """
        Rozpoczyna tury kolejnych jednostek danej armii
        """
        for unit in self.__unit_list:
            unit.move(board)

    def count_base_units(self):
        """Liczy żywe jednostki podstawowe."""
        pass

    def count_special_units(self):
        """Liczy żywe jednostki specjalne."""
        pass
