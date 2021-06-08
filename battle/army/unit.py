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

    def __init__(
        self,
        fraction: str,
        pos: Position,
        board: Board,
        health_points=config.BASE_UNIT_HP,
        strength=config.BASE_UNIT_STRENGTH,
        movement_points=config.BASE_UNIT_MOVEMENT_POINTS,
    ) -> None:
        self.__fraction = fraction
        self.__health_points = health_points
        self.__strength = strength
        self.__movement_points = movement_points
        self.__pos = pos
        self.__is_alive = True
        # przejmuje pole na którym się respi
        self.capture_the_field(board, pos)
    
    def change_health_points(self, value: int) -> None:
        """Zmienia ilosc punktów życia jednostki"""
        self.__health_points = value
    
    def change_strength(self, value: int) -> None:
        """Zmienia siłę jednostki"""
        self.__strength = value
    
    def change_movement_points(self, value: int) -> None:
        """Zmienia ilość punktów ruchu jednostki"""
        self.__movement_points = value
    
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

    def get_fraction(self) -> str:
        """Zwraca frakcje jednostki"""
        return self.__fraction
    
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

    def is_alive(self) -> bool:
        """
        Zwraca punkty życia jednostki
        """
        return self.__is_alive


class BaseUnit(Unit):
    """Podstawowa jednstka. Identyczna dla wszystkich armii."""

    def __init__(self, fraction: str, pos: Position, board: Board) -> None:
        super().__init__(fraction=fraction, pos=pos, board=board)
        

class SpecialUnitA(Unit):
    """Silniejsza i bardziej wytrzymala, walczy z kilkoma jednostkami."""

    def __init__(self, fraction: str, pos: Position, board: Board) -> None:
        super().__init__(fraction=fraction, pos=pos, board=board)
        self.change_health_points(config.SPECIAL_UNIT_HP)
        self.change_strength(config.SPECIAL_UNIT_STRENGTH)
        
        

    def fight(self, board: Board, pos: Position) -> None:
        """
        Wywołuje metodę get_damage na każdym obiekcie
        z listy obiektów znajdujących się na polu.
        """
        defense_modifier = board.board_fields[pos.y][pos.x].get_defense_modifier()
        enemies: list[Unit] = board.board_fields[pos.y][pos.x].get_units()
        for enemy in enemies:
            enemy.get_damage(self.get_strength() + defense_modifier)
            logger.debug("JEDNOSTKA SPECJALNA A - SIŁA: %d" % self.get_strength())
            if enemy.get_hp() <= 0:
                board.board_fields[pos.y][pos.x].remove_unit(enemy)
                enemy.just_die()
                logger.debug("Poległem :(")


class SpecialUnitB(Unit):
    """Jednostka posiadająca więcej punktów ruchu."""

    def __init__(self, fraction: str, pos: Position, board: Board):
        super().__init__(fraction=fraction, pos=pos, board=board)
        self.change_movement_points(config.SPECIAL_UNIT_MOVEMENT_POINT)


class SpecialUnitC(Unit):
    """Jednostka Przejmująca teren na dystans"""

    def __init__(self, fraction: str, pos: Position, board: Board) -> None:
        super().__init__(fraction=fraction, pos=pos, board=board)

    def capture_the_field(self, board: Board, pos: Position) -> None:
        """
        Zmienia przynależność pola do frakcji.
        Dodaje siebie do listy jednostek znajdujących się na nowym polu. 
        """

        def takeover_from_a_distance(self, board: Board, pos: Position):
            """
            Przejmuje kilka pól z dystansu.
            """
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
                    if board.is_it_free(target_pos2, self.get_fraction()) == 1:
                        board.board_fields[target_pos2.y][target_pos2.x].change_fraction(
                            self.get_fraction()
                        )

        logger.debug("Przejmuje pole %d, %d" % (pos.x, pos.y))
        board.board_fields[pos.y][pos.x].change_fraction(self.get_fraction())
        # przekazuje wskaźnik na obecnie aktywny obiekt jednostki
        board.board_fields[pos.y][pos.x].add_unit(self)
        takeover_from_a_distance(self, board, pos)

    

class SpecialUnitD(Unit):
    """Jednostka przejmująca kilka pól obok swojej pozycji"""
    def __init__(self, fraction, pos, board) -> None:
        super().__init__(fraction=fraction, pos=pos, board=board)
    
    def capture_the_field(self, board: Board, pos: Position) -> None:
        def capture_more_fields(self, board: Board, pos: Position) -> None:
            """ 
            przejmuje wszystkie pola z ktorymi sasiaduje i są wolne : np x=2, y=2 przejmuje:
            (1,1)(2,1)(3,1)
            (1,2)[2,2](3,2)
            (1,3)(2,3)(3,3)
            """
            for value in range(3):
                for value2 in range(3):
                    target_pos = Position(pos.y - 1 + value2, pos.x - 1 + value)
                    if (
                        board.is_it_free(
                            target_pos, self.get_fraction()
                        )
                        == 1
                    ):
                        board.board_fields[target_pos.x][
                            target_pos.y
                        ].change_fraction(self.get_fraction())
        
        logger.debug("Przejmuje pole %d, %d" % (pos.x, pos.y))
        board.board_fields[pos.y][pos.x].change_fraction(self.get_fraction())
        # przekazuje wskaźnik na obecnie aktywny obiekt jednostki
        board.board_fields[pos.y][pos.x].add_unit(self)
        capture_more_fields(self, board, pos)
    
    
