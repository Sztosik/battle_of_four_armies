import random

class Field:
    def __init__(self):
        self.__defense_modifier = random.randint(-10, 10)
        self.__units = []
        self.__fraction = "none"

    def count_units(self):
        """
        Liczy jednostki znajdujące się na polu
        """
        return len(self.__units)

    def add_unit(self, unit):
        """
        Dodaje jednostkę do listy jednostek na polu
        """
        print("jednostki na przejmowanym polu", len(self.__units))
        for jednostka in self.__units:
            print(" - ", id(jednostka))

        self.__units.append(unit)

        print("jednostki na przejmowanym polu po przejęciu", len(self.__units))
        for jednostka in self.__units:
            print(" - ", id(jednostka))

    def remove_unit(self, unit):
        """
        Usuwa jednostkę z listy jednostek na polu
        """
        print("zwalniam pole, moje id: ", id(unit))
        print("jednostki na zwalnianym polu", len(self.__units))
        for jednostka in self.__units:
            print(" - ", id(jednostka))

        if len(self.__units) != 0:
            self.__units.remove(unit)

        print("jednostki na zwalnianym polu po zwolniuniu", len(self.__units))
        for jednostka in self.__units:
            print(" - ", id(jednostka))

    def get_fraction(self) -> str:
        """
        Zwraca przynależność pola do frakcji.
        """
        return self.__fraction

    def get_defense_modifier(self) -> int:
        """
        Zwraca modyfikator obronności pola.
        """
        return self.__defense_modifier

    def get_units(self) -> list:
        """
        Zwraca listę jednostek znajdujących się na polu
        """
        return self.__units

    def change_fraction(self, fraction: str) -> None:
        """
        Zmienia przynależność pola do frakcji
        """
        self.__fra
