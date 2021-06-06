import sys
from queue import Queue

import pygame

import battle.simulation.config as config
import battle.visualization.consts as consts
from battle.board.board import Board
from battle.simulation.sim_context import BoardData

screen = pygame.display.set_mode((consts.WIDTH, consts.WIDTH))


# TODO: Zrobić z tego klasę
def is_occupied(unit_list):
    if len(unit_list) == 0:
        return False
    return True


def get_board_data(board: Board, board_x: int, board_y: int) -> list[BoardData]:
    board_data: list[BoardData] = []

    for x in range(board_x):
        for y in range(board_y):
            field_state = is_occupied(board.board_fields[y][x].get_units())
            if not board.board_fields[y][x].get_fraction() == "none":
                fieald_data = BoardData(
                    x=x,
                    y=y,
                    fraction=board.board_fields[y][x].get_fraction(),
                    isOccupied=field_state,
                )
                board_data.append(fieald_data)
    return board_data


def main_visualization(board_queue: Queue, board_x: int, board_y: int) -> None:
    pygame.init()
    pygame.display.set_caption("Visualization")
    screen.fill(consts.WHITE)

    while True:
        board = board_queue.get()
        board_data = get_board_data(board, board_x, board_y)

        draw_grid(board_data)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.delay(config.SINGLE_FRAME_DURATION)


def draw_grid(itr_fields_data: list[BoardData]) -> None:

    for field_data in itr_fields_data:
        rectangle = pygame.Rect(
            field_data.x * consts.BLOCK_SIZE,
            field_data.y * consts.BLOCK_SIZE,
            consts.BLOCK_SIZE,
            consts.BLOCK_SIZE,
        )
        if field_data.fraction == "Yellow":
            if field_data.isOccupied:
                pygame.draw.rect(screen, consts.YELLOW, rectangle, 0)
            else:
                pygame.draw.rect(screen, consts.YELLOW_ACCENT, rectangle, 0)
        elif field_data.fraction == "Red":
            if field_data.isOccupied:
                pygame.draw.rect(screen, consts.RED, rectangle, 0)
            else:
                pygame.draw.rect(screen, consts.RED_ACCENT, rectangle, 0)
        elif field_data.fraction == "Green":
            if field_data.isOccupied:
                pygame.draw.rect(screen, consts.GREEN, rectangle, 0)
            else:
                pygame.draw.rect(screen, consts.GREEN_ACCENT, rectangle, 0)
        elif field_data.fraction == "Blue":
            if field_data.isOccupied:
                pygame.draw.rect(screen, consts.BLUE, rectangle, 0)
            else:
                pygame.draw.rect(screen, consts.BLUE_ACCENT, rectangle, 0)
        else:
            pygame.draw.rect(screen, consts.WHITE, rectangle, 0)
