from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from win32api import GetSystemMetrics

from grid import Grid


screen_width, screen_height = 400, 600  # 924, 693; 1366, 768; 1920, 1080; GetSystemMetrics(0), GetSystemMetrics(1)
fps = 30
scale = 10
font = pygame.font.Font(None, 27)

pygame.init()
screen = pygame.display.set_mode((screen_height, screen_width))     # pygame.FULLSCREEN
clock = pygame.time.Clock()


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run_game
            run_game = False


def pressed_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        global run_game
        run_game = False


grids = [Grid(1, 20, 20, pygame.Color("red")), Grid(2, 380, 20, pygame.Color("blue"))]

for grid in grids:
    grid.add_ship(1, (1, 1), 0)
    grid.add_ship(3, (1, 4), 0)
    grid.add_ship(2, (1, 8), 0)
    grid.add_ship(2, (5, 1), 0)

    field = grid.get_field()
    count = 0
    print(grid)
    for line in field:
        print(count, line)
        count += 1

run_game = True
while run_game:

    events()
    pressed_keys()

    screen.fill(pygame.Color("white"))

    for grid in grids:
        grid.draw_grid(screen, font)

        grid.mouse_clik()

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
