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
        text = font.render(symbol, cfg.antialias, pygame.Color("black"))
        screen.blit(text, (w + 6 + cfg.photo_size[0], h))
        w += cfg.photo_size[0]
    # cfg.start_height = h + cfg.photo_size[0]


def draw_numbers(w, h):
    for i in range(10):
        text = font.render(str(i + 1), cfg.antialias, pygame.Color("black"))
        screen.blit(text, (w - (3 if i == 9 else 0), h + 3))
        h += cfg.photo_size[0]


def draw_grid(grid, w, h):
    w_start_func, h_start_func = w, h
    for line in grid.get_field():
        for element in line:
            screen.blit(cfg.space, (w, h))
            w += cfg.photo_size[0]
        w = w_start_func
        h += cfg.photo_size[1]
    pygame.draw.rect(screen, pygame.Color("gray"), (w_start_func, h_start_func, cfg.photo_size[0] * 10, cfg.photo_size[1] * 10), 1)


def draw_one_grid_with_symbols(grid, w_start, h_start):
    draw_symbols(w_start, h_start)
    h_start += cfg.photo_size[0]
    draw_numbers(w_start, h_start)
    w_start += cfg.photo_size[0]
    draw_grid(grid, w_start, h_start)

def main():
    pygame.init()
    player_1, player_2 = 0, 1
    grid_1 = Grid(player_1, player_2)
    grid_2 = Grid(player_2, player_1)
    # w, h = cfg.start_width, cfg.start_height
    global run_game
    while run_game:
        events()
        draw_one_grid_with_symbols(grid_1, 10, 10)
        draw_one_grid_with_symbols(grid_1, 250, 10)
        draw_one_grid_with_symbols(grid_2, 10, 320)
        draw_one_grid_with_symbols(grid_2, 250, 320)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

