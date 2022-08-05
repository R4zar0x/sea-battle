import pygame

import config as cfg
import constructor


def events(grids):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.game:
                cfg.game = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for grid in grids:
                if grid.cursor_in_grid():
                    cell_position = grid.get_cell_under_cursor()
                    line, element = cell_position[0], cell_position[1]
                    grid.click_on_grid(line, element)
