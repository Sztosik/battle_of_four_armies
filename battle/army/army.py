from battle.army.unit import BaseUnit, SpecialUnitA, SpecialUnitB, SpecialUnitC, SpecialUnitD, Unit
from battle.board.board import Board
from battle.simulation.sim_context import Position


class Army:
    """Przechowuje jednostki i zbiera ich statystyki."""

    def __init__(
        self,
        fraction: str,
        init_number_of_base_units: int,
        init_number_of_special_units: int,
        start_point: Position,
        board: Board,
    ):
        self.fraction = fraction
        self.__init_number_of_base_units = init_number_of_base_units
        self.__init_number_of_special_units = init_number_of_special_units
        self.__unit_list: list[Unit] = []
        self.__start_point = start_point

        self.generate_unit_list(board)

    def generate_unit_list(self, board: Board) -> None:
        """
        Tworzy obiekty jednostek należących do armii i dodaje je do listy
        """
        for _ in range(self.__init_number_of_base_units):
            new_unit: BaseUnit = BaseUnit(
                fraction=self.fraction, pos=self.__start_point, board=board
            )
            self.__unit_list.append(new_unit)
            
        if self.fraction == "Red":
            for _ in range(self.__init_number_of_special_units):
                new_special_unit: SpecialUnitA = SpecialUnitA(
                    fraction=self.fraction, pos=self.__start_point, board=board
                )
                self.__unit_list.append(new_special_unit)
        
        elif self.fraction == "Yellow":
            for _ in range(self.__init_number_of_special_units):
                new_special_unit: SpecialUnitC = SpecialUnitC(
                    fraction=self.fraction, pos=self.__start_point, board=board
                )
                self.__unit_list.append(new_special_unit)
        
        elif self.fraction == "Blue":
            for _ in range(self.__init_number_of_special_units):
                new_special_unit: SpecialUnitD = SpecialUnitD(
                    fraction=self.fraction, pos=self.__start_point, board=board
                )
                self.__unit_list.append(new_special_unit)
        
        elif self.fraction == "Green":
            for _ in range(self.__init_number_of_special_units):
                new_special_unit: SpecialUnitB = SpecialUnitB(
                    fraction=self.fraction, pos=self.__start_point, board=board
                )
                self.__unit_list.append(new_special_unit)

    def start(self, board: Board) -> None:
        """
        Rozpoczyna tury kolejnych jednostek danej armii
        """
        for unit in self.__unit_list:
            unit.move(board)

    def count_units(self) -> int:
        """Liczy żywe jednostki."""
        counter = 0
        for unit in self.__unit_list:
            if unit.is_alive():
                counter += 1
        return counter
