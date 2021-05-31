import random
from field import Field
import config


class Board:
    def __init__(self, board_x, board_y):
        self.board_fields = []
        self.__board_x = board_x
        self.__board_y = board_y
        self.generate_board()


    def generate_board(self):
        """
        Tworzy dwuwymiarową tablicę obiektów Field.
        """
        new_row = []
        for y in range(self.__board_y):
            for x in range(self.__board_x):
                new_field = Field()
                new_row.append(new_field)
            self.board_fields.append(new_row)
            new_row = []

    def is_it_free(self, x, y, fraction):
        """
        Sprawdza stan pola.
        """
        # sprawdza czy pole nie wychodzi poza skale
        if (x < 0 or x >= self.__board_x) or (y < 0 or y >= self.__board_y):
            return 0

        field = self.board_fields[y][x]

        # przypadek kiedy żadna jednostka nie stała na tym polu albo jest sojusznicze
        if field.get_fraction() == "none" or field.get_fraction() == fraction:
            return 1
        # kiedy na polu nie ma żadnej jednostki ale należy do przeciwnika
        elif field.count_units(self) == 0:
            return 1
        # na polu znajduje się co najmniej jedna jednostka przeciwna
        else:
            return 2

    def get_fields(self):
        """
        Generator pól należących do planszy
        """
        for y in range(self.__board_y):
            for x in range(self.__board_x):
                yield self.board_fields[y][x]

    def captured_fields(self):
        """
        Zwraca słownik z liczbą przejętych pól przez armie
        """
        fractions = config.FRACTION_NAMES
        fractions_dict = dict()

        for name in fractions:
            fractions_dict[name] = 0

        for field in self.get_fields():
            for name in fractions:
                if name == field.get_fraction():
                    fractions_dict[name] += 1
        return fractions_dict

    def get_all_fields_data(self):
        return self.board_fields


