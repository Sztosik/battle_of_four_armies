import random
import config

class Base_unit:
    def __init__(self, id, fraction, pos_x, pos_y):
        self.__id = id
        self.__fraction = fraction
        self.__health_points = config.BASE_UNIT_HP
        self.__strength = config.BASE_UNIT_STRENGTH
        self.__movement_points = config.BASE_UNIT_MOVMENT_POINT
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__is_alive = True

    def move(self, board):
        if self.__is_alive == True:
            movement = self.__movement_points
            while movement > 0:
                rand_x = random.randint(-1, 1)
                rand_y = random.randint(-1, 1)
                pos_x = self.__pos_x + rand_x
                pos_y = self.__pos_y + rand_y

                # zwraca 0: jeśli pole nie istnieje,  1: jeśli na polu nie ma przeciwnika,  2: na polu znajduje się przeciwnik
                move = board.is_it_free(pos_x, pos_y, self.__fraction)
                if move == 1:
                    # usuwa jednostkę z listy jednostek pola na którym stała wcześniej, przenieść to do funkcji captude_the_field
                    board.board_fields[pos_y][pos_x].remove_unit(self.__id)
                    # aktualizuje pozycje jednostki
                    self.__pos_x = pos_x
                    self.__pos_y = pos_y
                    self.capture_the_field(board, pos_x, pos_y)
                    movement -= 1
                if move == 2:
                    self.fight()
                    movement -= 1
    
    def capture_the_field(self, board, x, y):
        # zmienia przynależność pola
        board.board_fields[y][x].change_fraction(self.__fraction)
        # dodaje jednostkę do listy jednostek znajdujących się na tym polu
        board.board_fields[y][x].add_unit(self.__id)

    def fight(self, board, x, y):
        # id pierwszego przeciwnika znajdującego się na polu
        enemy_id = board.board_fields[y][x].get_units()[0]
        enemy_fraction = board.board_fields[y][x].get_fraction()
        # niech pole przechowuje nie id ale ardesy obiektów (jednostek) w pamięci i będzie git

    def get_demage(self):
        pass

    def die(self):
        self.__is_alive = False

class Unit_A:
    pass

class Unit_B:
    pass

class Unit_C:
    pass

class Unit_D:
    pass