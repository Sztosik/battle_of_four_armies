import sys
import time
from queue import Queue

import pygame

import battle.simulation.config as config
import battle.visualization.consts as consts
from battle.board.board import Board
from battle.simulation.sim_context import BoardData


def get_board_data(board: Board) -> list[BoardData]:
    board_data: list[BoardData] = []

    for field in board.get_fields():

        field_state = field.is_occupied()

        if not field.get_fraction() == "none":
            fieald_data = BoardData(
                x=field.position.x,
                y=field.position.y,
                fraction=field.get_fraction(),
                isOccupied=field_state,
            )
            board_data.append(fieald_data)

    return board_data


def main_visualization(board_queue: Queue) -> None:
    pygame.init()

    # czeka na pierwszy element kolejki
    board: Board
    while True:
        if not board_queue.empty():
            board = board_queue.get()
            break

    board_size = board.get_board_size()
    screen = pygame.display.set_mode(
        (board_size.y * consts.BLOCK_SIZE, board_size.y * consts.BLOCK_SIZE)
    )
    pygame.display.set_caption("Visualization")
    screen.fill(consts.WHITE)

    while True:
        board = board_queue.get()
        if board.end == True:
            break
        board_data = get_board_data(board)

        draw_grid(board_data, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.delay(config.SINGLE_FRAME_DURATION)

    while True:
        print("Symulacja zakończona")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.time.delay(1000)


def draw_grid(itr_fields_data: list[BoardData], screen) -> None:

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
