import logging

from battle.simulation.sim_context import Position

BASE_UNIT_HP = 100
SPECIAL_UNIT_HP = 300
BASE_UNIT_STRENGTH = 50
SPECIAL_UNIT_STRENGTH = 30
BASE_UNIT_MOVEMENT_POINTS = 1
SPECIAL_UNIT_MOVEMENT_POINT = 1
BOARD_X = 20
BOARD_Y = 20
FRACTION_NAMES = ["Red", "Green", "Blue", "Yellow"]
LOGGING_LEVEL = logging.CRITICAL

POS_RED = Position(40, 40)
POS_GREEN = Position(40, 60)
POS_BLUE = Position(60, 40)
POS_YELLOW = Position(60, 60)
