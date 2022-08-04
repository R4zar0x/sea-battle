from os import environ
from pprint import pprint

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
    grid_1 = Grid(player_1, player_2)
    grid_2 = Grid(player_2, player_1)
    # grid.set_positions(10, 10)
    start_button = Button(300, 200, 100, 50)
    start_button.set_text("Next player")
    start_button.set_function(menu.button_start_game, grid_1)

    while cfg.menu:

        menu.events(grid_1, start_button, 300, 50)
        # menu.events(grid_2, start_button, 300, 300)

        screen.fill(pygame.Color("white"))

        start_button.set_button_color(menu.button_color(grid_1))
        start_button.set_text_color(menu.button_color(grid_1))

        grid_1.draw_grid(screen, 10, 10)
        # grid_2.draw_grid(screen, 10, 250)

        constructor.draw_constructor(grid_1, 300, 50)
        # constructor.draw_constructor(grid_2, 300, 300)

        start_button.draw_button(screen)




        clock.tick(fps)
        pygame.display.flip()

    start_button.set_text("Start game")
    cfg.menu = True
    while cfg.menu:

        # menu.events(grid_1, start_button, 300, 50)
        menu.events(grid_2, start_button, 300, 300)

        screen.fill(pygame.Color("white"))

        start_button.set_button_color(menu.button_color(grid_2))
        start_button.set_text_color(menu.button_color(grid_2))

        # grid_1.draw_grid(screen, 10, 10)
        grid_2.draw_grid(screen, 10, 250)

        # constructor.draw_constructor(grid_1, 300, 50)
        constructor.draw_constructor(grid_2, 300, 300)

        start_button.draw_button(screen)




        clock.tick(fps)
        pygame.display.flip()
    # grid_1 = grid
    # grid_2 = Grid(player_2, player_1)
    # grid.set_positions(250, 10)

    # pprint(grid_1.get_field())
    # print("*******************************")
    # pprint(grid_2.get_field())

    # button_next_player = Button()

    while cfg.game:
        game.events()

        screen.fill(pygame.Color("white"))

        player
        grid_1.draw_grid(screen, 10, 10)
        grid_1.draw_grid(screen, 10, 300)
        grid_2.draw_grid(screen, 250, 10)
        grid_2.draw_grid(screen, 250, 300)

        clock.tick(fps)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
