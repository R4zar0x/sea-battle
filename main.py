from os import environ
from pprint import pprint

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

from button import Button
from local_grid import Grid
import config as cfg
from config import screen, fps, clock
import constructor
import menu
import game

pygame.init()

# TODO: считается общая сумма всех кораблей в меню (нужно сделать отдельное для каждого из игроков)
# TODO: при закрытии окна открывается следующее
# TODO: поменять цвет кнопки (зелёный слишком яркий)

def main():
    player_1, player_2 = 0, 1
    grid_1 = Grid(player_1, player_2)
    grid_2 = Grid(player_2, player_1)
    start_button = Button(300, 200, 100, 50)
    start_button.set_text("Next player")
    start_button.set_function(menu.button_start_game, grid_1)

    while cfg.menu:

        menu.events(grid_1, start_button, 300, 50)
        screen.fill(pygame.Color("white"))
        start_button.set_button_color(menu.button_color(grid_1))
        start_button.set_text_color(menu.button_color(grid_1))
        grid_1.draw_grid(screen, 10, 10, player=0)
        constructor.draw_constructor(grid_1, 300, 50)
        start_button.draw_button(screen)
        clock.tick(fps)
        pygame.display.flip()

    start_button.set_text("Start game")
    cfg.menu = True
    while cfg.menu:
        menu.events(grid_2, start_button, 300, 300)
        screen.fill(pygame.Color("white"))
        start_button.set_button_color(menu.button_color(grid_2))
        start_button.set_text_color(menu.button_color(grid_2))
        grid_2.draw_grid(screen, 10, 250, player=1)
        constructor.draw_constructor(grid_2, 300, 300)
        start_button.draw_button(screen)
        clock.tick(fps)
        pygame.display.flip()

    cfg.game = True
    while cfg.game:
        screen.fill(pygame.Color("white"))
        grid_1.draw_grid(screen, 10, 10, player=0)
        grid_2.draw_grid(screen, 10, 300, player=1)
        grid_2.draw_grid(screen, 250, 10, player=0)
        grid_1.draw_grid(screen, 250, 300, player=1)
        game.events([grid_1, grid_2])
        clock.tick(fps)
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
