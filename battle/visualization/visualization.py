import json
import sys

import pygame

import battle.visualization.consts as consts




def main_visualization(path, size_x: int, size_y: int) -> None:
    pygame.init()
    screen = pygame.display.set_mode((size_x * consts.BLOCK_SIZE, size_y * consts.BLOCK_SIZE))
    pygame.display.set_caption("Visualization")
    screen.fill(consts.WHITE)

    with open(path) as f:
        data = json.load(f)
    itr = 0
    while itr < len(data):
        draw_grid(data[itr], screen)
        itr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.delay(consts.SINGLE_FRAME_DURATION)

    while True:
        pass


def draw_grid(itr_fields_data, screen) -> None:

    for x in range(len(itr_fields_data)):
        rectangle = pygame.Rect(
            itr_fields_data[x]["x"] * consts.BLOCK_SIZE,
            itr_fields_data[x]["y"] * consts.BLOCK_SIZE,
            consts.BLOCK_SIZE,
            consts.BLOCK_SIZE,
        )
        if itr_fields_data[x]["fraction"] == "Yellow":
            if itr_fields_data[x]["isOccupied"]:
                pygame.draw.rect(screen, consts.YELLOW, rectangle, 0)
            else:
                pygame.draw.rect(screen, consts.YELLOW_ACCENT, rectangle, 0)
        elif itr_fields_data[x]["fraction"] == "Red":
            if itr_fields_data[x]["isOccupied"]:
                pygame.draw.rect(screen, consts.RED, rectangle, 0)
            else:
                pygame.draw.rect(screen, consts.RED_ACCENT, rectangle, 0)
        elif itr_fields_data[x]["fraction"] == "Green":
            if itr_fields_data[x]["isOccupied"]:
                pygame.draw.rect(screen, consts.GREEN, rectangle, 0)
            else:
                pygame.draw.rect(screen, consts.GREEN_ACCENT, rectangle, 0)
        elif itr_fields_data[x]["fraction"] == "Blue":
            if itr_fields_data[x]["isOccupied"]:
                pygame.draw.rect(screen, consts.BLUE, rectangle, 0)
            else:
                pygame.draw.rect(screen, consts.BLUE_ACCENT, rectangle, 0)
        else:
            pygame.draw.rect(screen, consts.WHITE, rectangle, 0)
