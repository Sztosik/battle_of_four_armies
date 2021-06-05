from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int


@dataclass
class BoardData:
    x: int
    y: int
    fraction: str
    isOccupied: bool
