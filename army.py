import config
import random
from board import Board

class Army:
    def __init__(self, fraction, init_number_of_base_units, init_number_of_special_units, start_point_x, start_point_y):
        self.__fraction = fraction
        self.__init_number_of_base_units = init_number_of_base_units
        self.__init_number_of_special_units = init_number_of_special_units
        self.__unit_list = []
        self.__start_point_x = start_point_x
        self.__start_point_y = start_point_y

        self.generate_base_unit_list()

    def generate_unit_list(self):
        for id in range(self.__init_number_of_base_units):
            new_unit = Base_unit(id, self.__fraction, self.__start_point_x, self.__start_point_y)
            self.__unit_list.append(new_unit)

        for id in range(self.__init_number_of_special_units):
            new_unit = Base_unit(id, self.__fraction, self.__start_point_x, self.__start_point_y)
            self.__unit_list.append(new_unit)

    def start(self, board):
        for unit in self.__unit_list:
            unit.move(board)

    def count_base_units(self):
        pass

    def count_special_units(self):
        pass



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

                move = board.is_it_free(pos_x, pos_y)
                if move == 1:
                    self.capture_the_field()
                    movement -= 1
                if move == 2:
                    self.fight()
    
    def capture_the_field(self):
        pass

    def fight(self):
        pass

    def die(self):
        self.__is_alive = False
