from dataclasses import dataclass


@dataclass
class Position:
    """
    Przechowuje położenie w układzie kartezjańskim.
    """
    x: int
    y: int


@dataclass
class BoardData:
    """
    Przechowuje statystyki planszy.
    """
    x: int
    y: int
    fraction: str
    isOccupied: bool


@dataclass
class UnitsStats:
    """
    Przechowuje statystyki jednostek armii.
    """
    fraction: int
    number_of_units: int
