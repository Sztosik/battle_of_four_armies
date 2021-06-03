import random

import config
import logging
from board import Board


logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)


class Unit:
    def __init__(
        self, id, fraction: str, pos_x: int, pos_y: int, board: Board
    ) -> Board:
        self.__id = id
        self.__fraction = fraction
        self.__health_points = config.Base_Unit_HP
        self.__strength = config.Base_Unit_STRENGTH
        self.__movement_points = config.Base_Unit_MOVEMENT_POINT
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__is_alive = True
        # przejmuje pole na którym się respi
        self.capture_the_field(board, pos_x, pos_y)

    def move(self, board: Board) -> None:
        """
        Sprawdza czy jednostka jest jeczsze żywa i czy ma punkty ruchu.
        Lusuje pole i sprawdza jego status i podejmuje decyzje o dalszych działaniach
        """

        logger.debug("\nTura jednostki: %d" % id(self))
        logger.debug("frakcja jednostki: %s" % self.__fraction)

        if self.__is_alive == True:
            movement = self.__movement_points

            while movement > 0:
                rand_x = random.randint(-1, 1)
                rand_y = random.randint(-1, 1)
                pos_x = self.__pos_x + rand_x
                pos_y = self.__pos_y + rand_y

                move = board.is_it_free(pos_x, pos_y, self.__fraction)
                # pole jest puste, albo stoi na nim sojusznik
                if move == 1:
                    logger.debug("pole które chce zwolnić: %d, %d" % (self.__pos_x, self.__pos_y))
                    # usuwa jednostkę z pola na którym stoi aktualnie
                    board.board_fields[self.__pos_y][self.__pos_x].remove_unit(self)
                    self.__pos_x = pos_x
                    self.__pos_y = pos_y
                    self.capture_the_field(board, pos_x, pos_y)
                    movement -= 1
                # na polu stoi co najmniej jedna wroga jednostka
                if move == 2:
                    self.fight(board, pos_x, pos_y)
                    movement -= 1

    def capture_the_field(self, board: Board, x: int, y: int) -> None:
        """
        Zmienia przynależność pola do frakcji.
        Dodaje siebie do listy jednostek znajdujących się na nowym polu
        """

        logger.debug("Przejmuje pole %d, %d" % (x, y))
        board.board_fields[y][x].change_fraction(self.__fraction)
        # przekazuje wskaźnik na obecnie aktywny obiekt jednostki
        board.board_fields[y][x].add_unit(self)

    def fight(self, board: Board, x: int, y: int) -> None:
        """
        Wywołuje metodę get_damage na pierwszym obiekcie
        z listy obiektów znajdujących się na polu.
        """
        defense_modifier = board.board_fields[y][x].get_defense_modifier()
        enemy = board.board_fields[y][x].get_units()[0]
        enemy.get_damage(
            self.get_strength() + defense_modifier
        )  # zwiększa lub zmniejsza silę bazową o 10
        if enemy.get_hp() <= 0:
            enemy.just_die()
        logger.critical("WALKA!!!")

    def get_damage(self, damage: float) -> None:
        """
        Zmienia stan punktów życia
        """
        logger.critical("Jestem atakowany!!!")

    def get_strength(self) -> int:
        """
        Zwraca punkty siły obiektu
        """
        return self.__strength

    def just_die(self) -> None:
        """
        Zmienia stan jednostki na martwy
        """
        self.__is_alive = False

    def get_hp(self) -> int:
        """
        Zwraca punkty życia jednostki
        """
        return self.__health_points


class Base_Unit(Unit):
    def __init__(self, id, fraction, pos_x, pos_y, board):
        super().__init__(id, fraction, pos_x, pos_y, board)


# silniejsza i bardziej wytrzymala, walczy z kilkoma jednostkami
class Special_Unit_A(Unit):
    def __init__(self, id, fraction, pos_x, pos_y):
        super().__init__(id, fraction, pos_x, pos_y)
        self.__health_points = config.SPECIAL_UNIT_HP
        self.__strength = config.SPECIAL_UNIT_STRENGTH

    def fight(self, board: Board, x: int, y: int) -> None:
        """
        Wywołuje metodę get_damage na każdym obiekcie
        z listy obiektów znajdujących się na polu.
        """
        defense_modifier = board.board_fields[y][x].get_defense_modifier()
        enemies = board.board_fields[y][x].get_units()
        for enemy in enemies:
            enemy.get_damage(self.get_strength() + defense_modifier)
            if enemy.get_hp() <= 0:
                enemy.just_die()


# wiecej movement pointsow
class Special_Unit_B(Unit):
    def __init__(self, id, fraction, pos_x, pos_y):
        super().__init__(id, fraction, pos_x, pos_y)
        self.__movement_points = config.SPECIAL_UNIT_MOVEMENT_POINT


# przejmowanie terernu z dystansu
class Special_Unit_C(Unit):
    def takeover_from_a_distance(self, board, x, y):
        throw_direction = random.randint(0, 3)  # 0:góra   1:prawo   2:dół   3:lewo
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
                if (
                    board.is_it_free(
                        target_pos_y - 1 + value,
                        target_pos_x - 1 + value2,
                        self.__fraction,
                    )
                    == 1
                ):
                    board.board_fields[target_pos_y - 1 + value][
                        target_pos_x - 1 + value2
                    ].change_fraction(self.__fraction)


# przejmuje pola sasiednie
class Special_Unit_D(Unit):

    # przejmuje wszystkie pola z ktorymi sasiaduje i są wolne : np x=2, y=2 przejmuje:
    # (1,1)(2,1)(3,1)
    # (1,2)[2,2](3,2)
    # (1,3)(2,3)(3,3)

    def capture_the_field(self, board, x, y):
        board.board_fields[y][x].add_unit(self.__id)
        for value in range(3):
            for value2 in range(3):
                if (
                    board.is_it_free(y - 1 + value, x - 1 + value2, self.__fraction)
                    == 1
                ):
                    board.board_fields[y - 1 + value][x - 1 + value2].change_fraction(
                        self.__fraction
                    )
