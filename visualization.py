import pygame
import consts
pygame.init()

screen = pygame.display.set_mode((consts.WIDTH, consts.WIDTH))
pygame.display.set_caption("Visualization")
screen.fill(consts.WHITE)
CLOCK = pygame.time.Clock()
run = True


class Field:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = consts.WHITE

    def change_fraction(self, fraction_color):
        self.color = fraction_color


def draw_grid(color):
    block_size = consts.BLOCK_SIZE
    for x in range(int(consts.WIDTH/block_size)):
        if x % 4 == 0:
            for y in range(int(consts.WIDTH/block_size)):
                rect = pygame.Rect(x*block_size, y*block_size,
                                   block_size, block_size)
                if y % 4 == 0:
                    pygame.draw.rect(screen, color, rect, 0)
                else:
                    pygame.draw.rect(screen, consts.GREEN_ACCENT, rect, 0)
        else:
            for y in range(int(consts.WIDTH/block_size)):
                rect = pygame.Rect(x*block_size, y*block_size,
                                   block_size, block_size)
                if y % 4 == 0:
                    pygame.draw.rect(screen, consts.YELLOW_ACCENT, rect, 0)
                else:
                    pygame.draw.rect(screen, consts.GREEN_ACCENT, rect, 0)


def main():
    itr = 0
    while run:
        if itr % 2 == 0:
            draw_grid(consts.BLUE_ACCENT)
        elif itr % 3 == 0:
            draw_grid(consts.YELLOW_FIGHT)
        else:
            draw_grid(consts.RED)
        itr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        pygame.time.wait(500)


main()
