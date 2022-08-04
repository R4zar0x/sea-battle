import pygame

import config as cfg
import constructor


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.game:
                cfg.game = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pass
