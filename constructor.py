import pygame

import config as cfg
from config import screen
from handler import Grid


def draw_constructor(grid):
    x, y = cfg.constructor_position[0], cfg.constructor_position[1]
    for type_of_ship in cfg.types_of_ships:
        count_of_ships = grid.get_possible_count_of_ships()
        # 150, 10, 10 red; 10, 150, 10 green
        color = pygame.Color(10, 150, 10) if count_of_ships[type_of_ship - 1] > 0 else pygame.Color(150, 10, 10)
        text_count_of_ships = cfg.font.render(f"{count_of_ships[type_of_ship - 1]} x",
                                              cfg.antialias, color)
        screen.blit(text_count_of_ships, (x - cfg.photo_size[0] * 1.2, y + cfg.photo_size[0] / 5))
        for length in range(type_of_ship):
            screen.blit(cfg.ship, (x, y))
            x += cfg.photo_size[0]
        x = cfg.constructor_position[0]
        y += cfg.photo_size[0] + 10

    if cfg.cursor != 0:
        mouse_position = pygame.mouse.get_pos()
        x, y = mouse_position[0] - cfg.photo_size[0] * 4 / 10, mouse_position[1] - cfg.photo_size[0] * 4 / 10
        for cell in range(cfg.cursor):
            screen.blit(cfg.ship, (x, y))
            if cfg.rotate:
                y += cfg.photo_size[0]
            else:
                x += cfg.photo_size[0]


def click_on_constructor(grid):
    if click_out_of_constructor() and cfg.cursor > 0:
        pygame.mouse.set_cursor(*cfg.cursor_normal)
        cfg.cursor = 0
    else:
        x, y = cfg.constructor_position[0], cfg.constructor_position[1]
        mouse_position = pygame.mouse.get_pos()

        for type_of_ship in cfg.types_of_ships:

            y_ship = y + (type_of_ship - 1) * (cfg.photo_size[0] + 10)

            if x <= mouse_position[0] < x + type_of_ship * cfg.photo_size[0] and \
                    y_ship <= mouse_position[1] < y_ship + cfg.photo_size[0]:

                if grid.get_possible_count_of_ships()[type_of_ship - 1]:

                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)

                    if cfg.cursor == type_of_ship:
                        cfg.rotate = not cfg.rotate
                    else:
                        cfg.rotate = False
                        cfg.cursor = type_of_ship
                else:
                    return


def click_out_of_constructor():
    x, y = cfg.constructor_position[0], cfg.constructor_position[1]
    mouse_position = pygame.mouse.get_pos()

    for type_of_ship in cfg.types_of_ships:
        y_ship = y + (type_of_ship - 1) * (cfg.photo_size[0] + 10)
        if x <= mouse_position[0] < x + type_of_ship * cfg.photo_size[0] and \
                y_ship <= mouse_position[1] < y_ship + cfg.photo_size[0]:
            return False
    return True


def add_ship(grid):
    cell_position = grid.get_cell_under_cursor()
    line = cell_position[0]
    element = cell_position[1]
    count_of_ships = grid.get_possible_count_of_ships()
    if grid.is_free_space_for_ship(cfg.rotate, line, element) and count_of_ships[cfg.cursor - 1] > 0:
        array_of_cells = []
        if cfg.rotate:
            if line + cfg.cursor <= 10:
                for cell in range(cfg.cursor):
                    array_of_cells.append([line + cell, element])
            else:
                return
        else:
            if element + cfg.cursor <= 10:
                for cell in range(cfg.cursor):
                    array_of_cells.append([line, element + cell])
            else:
                return
        pygame.mouse.set_cursor(*cfg.cursor_normal)
        cfg.cursor = 0
        grid.set_ship(array_of_cells)
    else:
        return
