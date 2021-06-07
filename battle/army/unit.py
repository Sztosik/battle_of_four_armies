import logging
import random
from abc import ABC

import battle.simulation.config as config
from battle.board.board import Board
from battle.simulation.sim_context import Position

logging.basicConfig(level=config.LOGGING_LEVEL)
logger = logging.getLogger(__name__)


class Unit(ABC):
    """Abstrakcyjna klasa jednostki"""

    def __init__(self, fraction: str, pos: Position, board: Board) -> None:
        self.__fraction = fraction
        self.__health_points = config.BASE_UNIT_HP
        self.__strength = config.BASE_UNIT_STRENGTH
        self.__movement_points = config.BASE_UNIT_MOVEMENT_POINTS
        self.__pos = pos
        self.__is_alive = True
        # przejmuje pole na którym się respi
        self.capture_the_field(board, pos)

    def move(self, board: Board) -> None:
        """
        Sprawdza czy jednostka jest jeczsze żywa i czy ma punkty ruchu.
        Lusuje pole i sprawdza jego status i podejmuje decyzje o dalszych działaniach
        """

        logger.debug("\nTura jednostki: %d", id(self))
        logger.debug("frakcja jednostki: %s", self.__fraction)

        if self.__is_alive:
            movement = self.__movement_points

            while movement > 0:
                rand_x = random.randint(-1, 1)
                rand_y = random.randint(-1, 1)

                new_pos = Position(self.__pos.x + rand_x, self.__pos.y + rand_y)

                move = board.is_it_free(new_pos, self.__fraction)
                # pole jest puste, albo stoi na nim sojusznik
                if move == 1:
                    logger.debug(
                        "pole które chce zwolnić: %d, %d" % (self.__pos.x, self.__pos.y)
                    )
                    # usuwa jednostkę z pola na którym stoi aktualnie
                    board.board_fields[self.__pos.y][self.__pos.x].remove_unit(self)
                    self.__pos = new_pos
                    self.capture_the_field(board, new_pos)
                    movement -= 1
                # na polu stoi co najmniej jedna wroga jednostka
                if move == 2:
                    self.fight(board, new_pos)
                    movement -= 1

    def capture_the_field(self, board: Board, pos: Position) -> None:
        """
        Zmienia przynależność pola do frakcji.
        Dodaje siebie do listy jednostek znajdujących się na nowym polu
        """

        logger.debug("Przejmuje pole %d, %d" % (pos.x, pos.y))
        board.board_fields[pos.y][pos.x].change_fraction(self.__fraction)
        # przekazuje wskaźnik na obecnie aktywny obiekt jednostki
        board.board_fields[pos.y][pos.x].add_unit(self)

    def fight(self, board: Board, pos: Position) -> None:
        """
        Wywołuje metodę get_damage na pierwszym obiekcie
        z listy obiektów znajdujących się na polu.
        """
        defense_modifier = board.board_fields[pos.y][pos.x].get_defense_modifier()
        enemy: Unit = board.board_fields[pos.y][pos.x].get_units()[0]
        enemy.get_damage(
            self.get_strength() + defense_modifier
        )  # zwiększa lub zmniejsza silę bazową o 10
        if enemy.get_hp() <= 0:
            board.board_fields[pos.y][pos.x].remove_unit(enemy)
            enemy.just_die()
            logger.debug("Poległem :(")

    def get_damage(self, damage: int) -> None:
        """
        Zmienia stan punktów życia
        """
        self.__health_points -= damage
        logger.debug("Jestem atakowany, moje HP: %d", self.__health_points)

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


class BaseUnit(Unit):
    """Podstawowa jednstka. Identyczna dla wszystkich armii."""

    def __init__(self, fraction, pos, board):
        super().__init__(fraction=fraction, pos=pos, board=board)


class SpecialUnitA(Unit):
    """Silniejsza i bardziej wytrzymala, walczy z kilkoma jednostkami."""

    def __init__(self, fraction, pos, board):
        super().__init__(fraction, pos, board)

        # TODO: W tym miejscu występuje błąd, pola nie zostają nadpisane
        self.__health_points = config.SPECIAL_UNIT_HP
        self.__strength = config.SPECIAL_UNIT_STRENGTH

    def fight(self, board: Board, pos: Position) -> None:
        """
        Wywołuje metodę get_damage na każdym obiekcie
        z listy obiektów znajdujących się na polu.
        """
        defense_modifier = board.board_fields[pos.y][pos.x].get_defense_modifier()
        enemies: list[Unit] = board.board_fields[pos.y][pos.x].get_units()
        for enemy in enemies:
            enemy.get_damage(self.get_strength() + defense_modifier)
            logger.critical("JEDNOSTKA SPECJALNA A - SIŁA: %d" % self.get_strength())
            if enemy.get_hp() <= 0:
                board.board_fields[pos.y][pos.x].remove_unit(enemy)
                enemy.just_die()
                logger.critical("Poległem :(")


# TODO
class SpecialUnitB(Unit):
    """Jednostka posiadająca więcej punktów ruchu."""

    def __init__(self, fraction, pos: Position, board: Board):
        super().__init__(fraction, pos, board)
        self.__movement_points = config.SPECIAL_UNIT_MOVEMENT_POINT


# TODO
class SpecialUnitC(Unit):
    """Jednostka Przejmująca teren na dystans"""

    def takeover_from_a_distance(self, board: Board, pos: Position):
        throw_direction = random.randint(0, 3)  # 0:góra   1:prawo   2:dół   3:lewo
        throw_distance = random.randint(2, 10)

        if throw_direction == 0:
            target_pos = Position(pos.x, pos.y - throw_distance)

        elif throw_direction == 1:
            target_pos = Position(pos.x + throw_distance, pos.y)

        elif throw_direction == 2:
            target_pos = Position(pos.x, pos.y + throw_distance)

        elif throw_direction == 3:
            target_pos = Position(pos.x - throw_distance, pos.y)

        for value in range(3):
            for value2 in range(3):
                target_pos2 = Position(
                    target_pos.x - 1 + value2, target_pos.y - 1 + value
                )
                if board.is_it_free(target_pos2, self.__fraction) == 1:
                    board.board_fields[target_pos2.y][target_pos2.x].change_fraction(
                        self.__fraction
                    )


# TODO
# przejmuje pola sasiednie
class SpecialUnitD(Unit):

    # BRAKUJE TUTAJ KONSTRUKTORA

    # przejmuje wszystkie pola z ktorymi sasiaduje i są wolne : np x=2, y=2 przejmuje:
    # (1,1)(2,1)(3,1)
    # (1,2)[2,2](3,2)
    # (1,3)(2,3)(3,3)

    def capture_the_field(self, board, pos):
        board.board_fields[pos.y][pos.x].add_unit(self)
        for value in range(3):
            for value2 in range(3):
                if (
                    board.is_it_free(
                        pos.y - 1 + value, pos.x - 1 + value2, self.__fraction
                    )
                    == 1
                ):
                    board.board_fields[pos.y - 1 + value][
                        pos.x - 1 + value2
                    ].change_fraction(self.__fraction)
