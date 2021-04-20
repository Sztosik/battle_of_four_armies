import config
import random

class Board:
    def __init__(self):
        self.__board_fields = []
        self.generate_board()

    def generate_board(self):
        new_row = []
        for y in range(config.BOARD_Y):
            for x in range(config.BOARD_X): 
               new_field = Field(x, y)
               new_row.append(new_field)
            self.__board_fields.append(new_row)
            new_row = []

    def is_it_free(self, x, y, fraction):
        # sprawdza czy pole nie wychodzi poza skale
        if x < 0 or x >= config.BOARD_X or y < 0 or y >= config.BOARD_Y:
            return 0

        field = self.__board_fields[y][x]

        # przypadek kiedy żadna jednostka nie stała na tym polu albo jest sojusznicze
        if field.get_fraction() == "none" or field.get_fraction() == fraction: 
            return 1
        elif field.count_units(self) == 0:
            return 1
        else:
            return 2

    

class Field:
    def __init__(self, pos_x, pos_y):
        self.__defense_modifier = random.randint(-10, 10)
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__units = []
        self.__fraction = "none"
        
    def count_units(self):
        return len(self.__units)

    def add_unit(self, unit):
        self.__units.append(unit)
    
    def get_fraction(self):
        return self.__fraction

    def get_defense_modifier(self):
        return self.__defense_modifier

    def change_fraction(self, fraction):
        self.__fraction = fraction