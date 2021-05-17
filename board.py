import random

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


class Field:
    def __init__(self):
        self.__defense_modifier = random.randint(-10, 10)
        self.__units = []
        self.__fraction = "none"

    def count_units(self):
        """
        Liczy jednostki znajdujące się na polu
        """
        return len(self.__units)

    def add_unit(self, unit):
        print("jednostki na przejmowanym polu", len(self.__units))
        for jednostka in self.__units:
            print(" - ", id(jednostka))

        self.__units.append(unit)

        print("jednostki na przejmowanym polu po przejęciu", len(self.__units))
        for jednostka in self.__units:
            print(" - ", id(jednostka))

    # sprawdzić czy ta funkcja usuwa jednostkę o podanym id z listy
    def remove_unit(self, unit):
        print("zwalniam pole, moje id: ", id(unit))
        print("jednostki na zwalnianym polu", len(self.__units))
        for jednostka in self.__units:
            print(" - ", id(jednostka))

        if len(self.__units) != 0:
            self.__units.remove(unit)

        print("jednostki na zwalnianym polu po zwolniuniu", len(self.__units))
        for jednostka in self.__units:
            print(" - ", id(jednostka))

    def get_fraction(self):
        return self.__fraction

    def get_defense_modifier(self):
        return self.__defense_modifier

    def get_units(self):
        return self.__units

    def change_fraction(self, fraction):
        self.__fraction = fraction
