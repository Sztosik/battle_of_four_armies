from unit import Base_unit

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



