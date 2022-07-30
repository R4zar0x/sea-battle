from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pprint import pprint
from win32api import GetSystemMetrics

from handler import Ship, Grid
import config as cfg
from config import screen, fps, clock, font

run_game = True


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run_game
            run_game = False


def draw_symbols(w, h):
    for symbol in cfg.symbols:
        text = font.render(symbol, True, pygame.Color("black"))
        screen.blit(text, (w, h - cfg.photo_size[0]))
        w += cfg.photo_size[0]
    # cfg.start_height = h + cfg.photo_size[0]


def draw_grid(grid, w, h):
    for line in grid.get_field():
        for element in line:
            screen.blit(cfg.space, (w, h))
            w += cfg.photo_size[0]
        w = cfg.start_width
        h += cfg.photo_size[1]
    pygame.draw.rect(screen, pygame.Color("gray"), (cfg.start_width, cfg.start_height, cfg.photo_size[0] * 10, cfg.photo_size[1] * 10), 1)


def main():
    pygame.init()
    # cfg.start_height += 100
    w, h = cfg.start_width, cfg.start_height
    player_1, player_2 = 0, 1
    grid_1 = Grid(player_1, player_2)
    grid_2 = Grid(player_2, player_1)

    # pprint(grid_1.get_field())
    # pprint(grid_2.get_field())
    global run_game
    while run_game:
        events()


        draw_symbols(w, h)
        draw_grid(grid_1, w, h)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

