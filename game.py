import pygame

import config as cfg
import constructor
from local_grid import Grid


def events(grids):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.game:
                cfg.game = False
                cfg.run = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for grid in grids:
                if cfg.game_mode == cfg.game_mods[3 - grid.get_player()]:
                    if grid.cursor_in_grid():
                        cell_position = grid.get_cell_under_cursor()
                        line, element = cell_position[0], cell_position[1]
                        grid.click_on_grid(line, element)
                        # grid.change_game_mode()
                        if not grid.is_player_has_ships():
                            cfg.game = False
                            cfg.winner = grids[1 - grid.get_player()].get_player_name()
