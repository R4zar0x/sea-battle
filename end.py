import pygame

import config as cfg


def events(buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.end:
                cfg.end = False
                cfg.run = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for button in buttons:
                if button.is_mouse_on_button():
                    button.button_click()


def button_exit():
    cfg.end = False
    cfg.run = False


def button_restart():
    cfg.end = False
    cfg.menu = True


def draw_text(surface, x, y, text, text_color=pygame.Color("lightblue")):
    txt = cfg.end_font.render(text, True, text_color)
    surface.blit(txt, (x - txt.get_width() / 2, y))
