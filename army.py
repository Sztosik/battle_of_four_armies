from unit import Unit, Base_Unit

class Army:
    def __init__(self, fraction, init_number_of_Base_Units, init_number_of_special_units, start_point_x, start_point_y, board):
        self.fraction = fraction
        self.__init_number_of_Base_Units = init_number_of_Base_Units
        self.__init_number_of_special_units = init_number_of_special_units
        self.__unit_list = []
        self.__start_point_x = start_point_x
        self.__start_point_y = start_point_y

        self.generate_unit_list(board)

    def generate_unit_list(self, board):
        for id in range(self.__init_number_of_Base_Units):
            new_unit = Base_Unit(id, self.fraction, self.__start_point_x, self.__start_point_y, board)
            self.__unit_list.append(new_unit)

        # for id in range(self.__init_number_of_special_units):
        #     new_unit = Base_Unit(id, self.fraction, self.__start_point_x, self.__start_point_y)
        #     self.__unit_list.append(new_unit)

    def start(self, board):
        for unit in self.__unit_list:
            unit.move(board)

    def count_Base_Units(self):
        pass

    def count_special_units(self):
        pass



