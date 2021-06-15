import battle.simulation.config as config
from battle.board.field import Field
from battle.simulation.sim_context import Position


class Board:
    """
    Klasa przechowująca planszę.

    Robi dwie rzeczy:
    1. Generuje nową planszę
    2. Zwraca stany pól
    """

    def __init__(self, board_x: int, board_y: int):
        self.board_fields: list[list[Field]] = []
        self.__board_x = board_x
        self.__board_y = board_y
        self.end = False
        self.generate_board()

    def generate_board(self) -> None:
        """
        Tworzy dwuwymiarową tablicę obiektów Field.

        :return: None
        """
        row: list[Field] = []
        for y in range(self.__board_y):
            for x in range(self.__board_x):
                field = Field(Position(x, y))
                row.append(field)
            self.board_fields.append(row)
            row = []

    def is_it_free(self, pos: Position, fraction: str) -> int:
        """
        Sprawdza stan pola.

        Zwraca:
        0 - jeśli pole nie istnieje,
        1 - żadna jednostka nie stała na tym polu albo jest sojusznicze,
        1 - na polu nie ma żadnej jednostki, ale należy do przeciwnika,
        2 - na polu znajduje się wroga jednostka

        :param pos: pozycja pola na planszy
        :return: int
        
        """

        # pole nie istnieje
        if (pos.x < 0 or pos.x >= self.__board_x) or (
            pos.y < 0 or pos.y >= self.__board_y
        ):
            return 0

        field = self.board_fields[pos.y][pos.x]

        # żadna jednostka nie stała na tym polu albo jest sojusznicze
        if field.get_fraction() == "none" or field.get_fraction() == fraction:
            return 1
        # na polu nie ma żadnej jednostki, ale należy do przeciwnika
        if field.count_units() == 0:
            return 1
        # na polu znajduje się co najmniej jedna jednostka przeciwna
        return 2

    def get_fields(self) -> Field:
        """
        Generator pól należących do planszy.

        :yield: Field
        """
        for y in range(self.__board_y):
            for x in range(self.__board_x):
                yield self.board_fields[y][x]

    def get_board_size(self) -> Position:
        """
        Zwraca wymiary planszy.
        
        :return: Position
        """
        return Position(self.__board_x, self.__board_y)

    def captured_fields(self) -> dict:
        """
        Zwraca słownik z liczbą przejętych pól przez armie

        :return: dict
        """
        fractions = config.FRACTION_NAMES
        fractions_dict: dict = dict()

        for name in fractions:
            fractions_dict[name] = 0

        for field in self.get_fields():
            for name in fractions:
                if name == field.get_fraction():
                    fractions_dict[name] += 1
        return fractions_dict

    def get_all_fields_data(self) -> list[list[Field]]:
        """
        Zwraca aktualny stan planszy.

        :return: list[list[Field]]
        """
        return self.board_fields
