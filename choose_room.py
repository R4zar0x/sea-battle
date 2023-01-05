import pygame

import config as cfg

def events(buttons, page):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.choose_room:
                cfg.choose_room = False
                cfg.run = False
        for button in buttons:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if button.is_mouse_on_button():
                    button.button_click()
        page.handler(event)