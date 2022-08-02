import pygame

import config as cfg
from config import screen


def draw_constructor():
    x, y = cfg.constructor_position[0], cfg.constructor_position[1]
    for type_of_ship in cfg.types_of_ships:
        for length in range(type_of_ship):
            screen.blit(cfg.ship, (x, y))
            x += cfg.photo_size[0]
        x = cfg.constructor_position[0]
        y += cfg.photo_size[0] + 10

    if cfg.cursor != 0:
        try:
            mouse_position = pygame.mouse.get_pos()
            x, y = mouse_position[0] - cfg.photo_size[0] * 4 / 10, mouse_position[1] - cfg.photo_size[0] * 4 / 10
            for cell in range(cfg.cursor):
                screen.blit(cfg.ship, (x, y))
                if cfg.rotate:
                    y += cfg.photo_size[0]
                else:
                    x += cfg.photo_size[0]
        except:
            pass


def is_clicked_on_constructor():
    x, y = cfg.constructor_position[0], cfg.constructor_position[1]
    mouse_position = pygame.mouse.get_pos()

    for type_of_ship in cfg.types_of_ships:
        y_ship = y + (type_of_ship - 1) * (cfg.photo_size[0] + 10)
        if x <= mouse_position[0] < x + type_of_ship * cfg.photo_size[0] and \
                y_ship <= mouse_position[1] < y_ship + cfg.photo_size[0]:
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            if cfg.cursor == type_of_ship:
                cfg.rotate = not cfg.rotate
            else:
                cfg.rotate = False
                cfg.cursor = type_of_ship


