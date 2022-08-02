from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pprint import pprint
from win32api import GetSystemMetrics

from handler import Ship, Grid
import config as cfg
from config import screen, fps, clock, font
import constructor

pygame.init()

run_game = True


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run_game
            run_game = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            constructor.is_clicked_on_constructor()


def main():
    player_1, player_2 = 0, 1
    grid_1 = Grid(player_1, player_2, 10, 10)

    global run_game
    while run_game:
        events()

        screen.fill(pygame.Color("white"))

        grid_1.draw_grid(screen)

        constructor.draw_constructor()

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
