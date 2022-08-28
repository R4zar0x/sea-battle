import pygame

import config as cfg
import constructor
from local_grid import Grid
from input_box import Box
from button import Button


def events(grid, button=0, box=0, x=0, y=0):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.menu:
                cfg.menu = False
                cfg.run = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if constructor.click_out_of_constructor(x, y):
                if grid.cursor_in_grid() and cfg.cursor > 0:
                    constructor.add_ship(grid)
                elif button.is_mouse_on_button() and cfg.cursor == 0:
                    button.button_click()
            else:
                constructor.click_on_constructor(grid, x, y)
        elif event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_f] and not box.get_active():
                constructor.demo_ships(grid)
        box.handle_event(event)


def button_next(grid):
    summ = 0
    for max_ships in grid.get_possible_count_of_ships():
        summ += max_ships
    if summ == 0:
        cfg.menu = False
        cfg.game = True
    return


def button_color(grid):
    summa = 0
    for max_ships in grid.get_possible_count_of_ships():
        summa += max_ships
    if summa == 0:
        return 10, 255, 10
    else:
        return 255, 10, 10


def text_draw(surface, grid, x, y, text_color=pygame.Color("gray")):
    text = f"Set name for {grid.get_player() + 1} player:"
    txt = cfg.font.render(text, True, text_color)
    surface.blit(txt, (x, y))
