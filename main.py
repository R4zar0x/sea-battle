from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

from button import Button
from handler import Grid
import config as cfg
from config import screen, fps, clock
import constructor
import menu
import game

pygame.init()


def main():
    player_1, player_2 = 0, 1
    grid = Grid(player_1, player_2, 10, 10)
    start_button = Button(300, 200, 100, 50)
    start_button.set_text("Start Game")
    start_button.set_function(menu.button_start_game, grid)

    while cfg.menu:
        menu.events(grid, start_button)

        screen.fill(pygame.Color("white"))

        grid.draw_grid(screen)

        constructor.draw_constructor(grid)

        start_button.draw_button(screen)

        clock.tick(fps)
        pygame.display.flip()

    grid_1 = grid
    grid_2 = Grid(player_2, player_1, 250, 10)
    # button_next_player = Button()

    while cfg.game:
        game.events()

        screen.fill(pygame.Color("white"))

        grid_1.draw_grid(screen)
        grid_2.draw_grid(screen)

        clock.tick(fps)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()