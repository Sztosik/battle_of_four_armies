import config
import random

class Board:
    def __init__(self, board_x, board_y):
        self.__board_fields = []
        self.__board_x = board_x
        self.__board_y = board_y
        self.generate_board()

    def generate_board(self):
        # tworzy dwuwymiarową tablicę obiektów Field
        new_row = []
        for y in range(self.__board_y):
            for x in range(self.__board_x): 
               new_field = Field(x, y)
               new_row.append(new_field)
            self.__board_fields.append(new_row)
            new_row = []

    def is_it_free(self, x, y, fraction):
        # sprawdza czy pole nie wychodzi poza skale
        if (x < 0 or x >= self.__board_x) or (y < 0 or y >= self.__board_y):
            return 0

        field = self.__board_fields[y][x]

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