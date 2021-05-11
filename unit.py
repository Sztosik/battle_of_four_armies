import random
import config

class Unit:
    def __init__(self, id, fraction, pos_x, pos_y, board):
        self.__id = id
        self.__fraction = fraction
        self.__health_points = config.Base_Unit_HP
        self.__strength = config.Base_Unit_STRENGTH
        self.__movement_points = config.Base_Unit_MOVEMENT_POINT
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__is_alive = True

        self.capture_the_field(board, pos_x, pos_y)


    def move(self, board):
        print("\nTura jednostki: ", id(self))
        print("frakcja jednostki: ", self.__fraction)
        if self.__is_alive == True:
            movement = self.__movement_points
            while movement > 0:
                rand_x = random.randint(-1, 1)
                rand_y = random.randint(-1, 1)
                pos_x = self.__pos_x + rand_x
                pos_y = self.__pos_y + rand_y

                move = board.is_it_free(pos_x, pos_y, self.__fraction)
                if move == 1:
                    print("pole które chce zwolnić: ", self.__pos_x, self.__pos_y)
                    board.board_fields[self.__pos_y][self.__pos_x].remove_unit(self) # przekazuje wskaźnik na obecnie aktywny obiekt jednostki
                    self.__pos_x = pos_x
                    self.__pos_y = pos_y
                    self.capture_the_field(board, pos_x, pos_y)
                    movement -= 1
                if move == 2:
                    self.fight()
                    movement -=1


    def capture_the_field(self, board, x, y):
            print("Przejmuje pole ",x, y)
            board.board_fields[y][x].change_fraction(self.__fraction)
            board.board_fields[y][x].add_unit(self) # przekazuje wskaźnik na obecnie aktywny obiekt jednostki

    def fight(self, board, x, y):
        # enemy_id = board.board_fields[y][x].get_units()[0]
        # enemy_fraction = board.board_fields[y][x].get_fraction()
        print("Walka")

class Base_Unit(Unit):
    def __init__(self, id, fraction, pos_x, pos_y, board):
        super().__init__(id, fraction, pos_x, pos_y, board)



#silniejsza i bardziej wytrzymala, walczy z kilkoma jednostkami
class Special_Unit_A(Unit):
    def __init__(self, id, fraction, pos_x, pos_y):
        super().__init__(id, fraction, pos_x, pos_y)
        self.__health_points = config.SPECIAL_UNIT_HP
        self.__strength = config.SPECIAL_UNIT_STRENGTH

#wiecej movement pointsow
class Special_Unit_B(Unit):
    def __init__(self, id, fraction, pos_x, pos_y):
        super().__init__(id, fraction, pos_x, pos_y)
        self.__movement_points = config.SPECIAL_UNIT_MOVEMENT_POINT

#przejmowanie terernu z dystansu
class Special_Unit_C(Unit):

    def takeover_from_a_distance(self, board, x ,y):
        throw_direction = random.randint(0, 3) # 0:góra   1:prawo   2:dół   3:lewo
        throw_distance = random.randint(2, 10)

        if throw_direction == 0:
            target_pos_x = x
            target_pos_y = y - throw_distance

        elif throw_direction == 1:
            target_pos_x = x + throw_distance
            target_pos_y = y

        elif throw_direction == 2:
            target_pos_x = x
            target_pos_y = y + throw_distance

        elif throw_direction == 3:
            target_pos_x = x - throw_distance
            target_pos_y = y

        for value in range(3):
            for value2 in range(3):
                if board.is_it_free(target_pos_y-1+value,target_pos_x-1+value2, self.__fraction) == 1:
                    board.board_fields[target_pos_y-1+value][target_pos_x-1+value2].change_fraction(self.__fraction)

#przejmuje pola sasiednie
class Special_Unit_D(Unit):

    #przejmuje wszystkie pola z ktorymi sasiaduje i są wolne : np x=2, y=2 przejmuje:
    # (1,1)(2,1)(3,1)
    # (1,2)[2,2](3,2)
    # (1,3)(2,3)(3,3)

    def capture_the_field(self, board, x, y):
            board.board_fields[y][x].add_unit(self.__id)
            for value in range(3):
                for value2 in range(3):
                    if board.is_it_free(y-1+value, x-1+value2, self.__fraction) == 1:
                        board.board_fields[y-1+value][x-1+value2].change_fraction(self.__fraction)
