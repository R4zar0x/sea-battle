import pygame

import config as cfg
import constructor


def events(grid, button, x, y):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.menu:
                cfg.menu = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if constructor.click_out_of_constructor(x, y):
                if grid.cursor_in_grid() and cfg.cursor > 0:
                    constructor.add_ship(grid)
                elif button.is_mouse_on_button() and cfg.cursor == 0:
                    button.button_click()
            else:
                constructor.click_on_constructor(grid, x, y)


def button_start_game(grid):
    summ = 0
    for max_ships in grid.get_possible_count_of_ships():
        summ += max_ships
    if summ == 0:
        grid.get_field()
        cfg.menu = False
        cfg.game = True
    return


def button_color(grid):
    summ = 0
    for max_ships in grid.get_possible_count_of_ships():
        summ += max_ships
    if summ == 0:
        return 0, 255, 0
    else:
        return 255, 0, 0
