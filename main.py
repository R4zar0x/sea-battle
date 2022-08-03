from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pprint import pprint
from win32api import GetSystemMetrics

from button import Button
from handler import Grid
import config as cfg
from config import screen, fps, clock, font
import constructor

pygame.init()

run_game = True

# TODO: Сделать так, чтобы нельзя было выбрать корабль, если тип кораблей с данным количеством палуб уже полностью выставлен
# TODO: Добавить новую фичу. Её действие: "При нажатии на сетку (без "корабля в руке") на существующий корабль, он удаляется"

def events(grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run_game
            run_game = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if grid.cursor_in_grid() and cfg.cursor > 0:
                constructor.add_ship(grid)
            else:
                constructor.click_on_constructor()


def main():
    player_1, player_2 = 0, 1
    grid_1 = Grid(player_1, player_2, 10, 10)
    button = Button(300, 200, 100, 50)
    button.set_text("Start Game")

    global run_game
    while run_game:
        events(grid_1)

        screen.fill(pygame.Color("white"))

        grid_1.draw_grid(screen)

        constructor.draw_constructor(grid_1)

        button.draw_button(screen)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
