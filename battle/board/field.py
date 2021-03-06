import random

from battle.simulation.sim_context import Position


class Field:
    """
    Klasa pola plaszy.

    Przechowuje chrakterystykę oraz stan pola.
    """

    def __init__(self, position: Position):
        self.__defense_modifier: int = random.randint(-10, 10)
        self.__units: list = []
        self.__fraction: str = "none"
        self.position = position

    def count_units(self) -> int:
        """
        Liczy jednostki znajdujące się na polu

        :return: int
        """
        return len(self.__units)

    def add_unit(self, unit) -> None:
        """
        Dodaje jednostkę do listy jednostek na polu
        
        :param unit: obiekt jednostki
        :return: None
        """
        self.__units.append(unit)

    def remove_unit(self, unit) -> None:
        """
        Usuwa jednostkę z listy jednostek na polu.

        :param unit: obiekt jednostki
        :return: None
        """
        if len(self.__units) != 0:
            self.__units.remove(unit)

    def get_fraction(self) -> str:
        """
        Zwraca przynależność pola do frakcji.

        :return: str
        """
        return self.__fraction

    def get_defense_modifier(self) -> int:
        """
        Zwraca modyfikator obronności pola.

        :return: int
        """
        return self.__defense_modifier

    def get_units(self) -> list:
        """
        Zwraca listę jednostek znajdujących się na polu

        :return: list[Unit]
        """
        return self.__units

    def change_fraction(self, fraction: str) -> None:
        """
        Zmienia przynależność pola do frakcji

        :param fraction: nazwa frakcji
        :return: None
        """
        self.__fraction = fraction

    def is_occupied(self) -> bool:
        """
        Informuje czy pole jest okupowane przez dowolną armię.

        :return: bool
        """
        if len(self.__units) == 0:
            return False
        return True
