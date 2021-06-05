import random


class Field:
    """
    Klasa pola plaszy.

    Przechowuje chrakterystykę oraz stan pola.
    """

    def __init__(self):
        self.__defense_modifier: int = random.randint(-10, 10)
        self.__units: list = []
        self.__fraction: str = "none"

    def count_units(self):
        """Liczy jednostki znajdujące się na polu"""
        return len(self.__units)

    def add_unit(self, unit):
        """Dodaje jednostkę do listy jednostek na polu"""
        self.__units.append(unit)

    def remove_unit(self, unit):
        """Usuwa jednostkę z listy jednostek na polu."""
        if len(self.__units) != 0:
            self.__units.remove(unit)

    def get_fraction(self) -> str:
        """Zwraca przynależność pola do frakcji."""
        return self.__fraction

    def get_defense_modifier(self) -> int:
        """Zwraca modyfikator obronności pola."""
        return self.__defense_modifier

    def get_units(self) -> list:
        """Zwraca listę jednostek znajdujących się na polu"""
        return self.__units

    def change_fraction(self, fraction: str) -> None:
        """Zmienia przynależność pola do frakcji"""
        self.__fraction = fraction
