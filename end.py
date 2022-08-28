import pygame

import config as cfg


def events(button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.end:
                cfg.end = False
                cfg.run = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if button.is_mouse_on_button():
                button.button_click()


def button_end():
    cfg.end = False
    cfg.run = False


def draw_text(surface, x, y, text, text_color=pygame.Color("lightblue")):
    txt = cfg.end_font.render(text, True, text_color)
    surface.blit(txt, (x - txt.get_width() / 2, y))
