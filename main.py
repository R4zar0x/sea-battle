from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pprint import pprint
from win32api import GetSystemMetrics

from handler import Ship, Grid
from config import screen, fps, clock

run_game = True


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run_game
            run_game = False


def drow_grid():
    pygame.draw.rect(screen, pygame.Color("black"), (50, 60, 100, 10), 1)


def main():
    pygame.init()
    player_1, player_2 = 0, 1
    grid_1 = Grid(player_1, player_2)
    grid_2 = Grid(player_2, player_1)

    # pprint(grid_1.get_field())
    # pprint(grid_2.get_field())
    global run_game
    while run_game:
        events()

        drow_grid()

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

