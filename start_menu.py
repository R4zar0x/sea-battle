import pygame

import config as cfg


def events(buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.start_menu:
                cfg.start_menu = False
                cfg.run = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for button in buttons:
                if button.is_mouse_on_button():
                    button.button_click()


def text_draw(surface, x, y, text, text_color=pygame.Color("lightblue")):
    txt = cfg.end_font.render(text, True, text_color)
    surface.blit(txt, (x - txt.get_width() / 2, y))


def button_start():
    cfg.start_menu = False


def button_settings():
    pass


def button_exit():
    cfg.start_menu = False
    cfg.run = False
