import pygame

import config as cfg
import constructor


def events(grid, button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.menu:
                cfg.menu = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if constructor.click_out_of_constructor():
                if grid.cursor_in_grid() and cfg.cursor > 0:
                    constructor.add_ship(grid)
                elif button.is_mouse_on_button() and cfg.cursor == 0:
                    button.button_click()
            else:
                constructor.click_on_constructor(grid)


def button_start_game(grid):
    grid.get_field()
    cfg.menu = False
    cfg.game = True
