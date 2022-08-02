from os import environ
from xml.dom.minidom import Element
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pprint import pprint
from win32api import GetSystemMetrics

from handler import Ship, Grid
import config as cfg
from config import screen, fps, clock, font

run_game = True


def events(grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run_game
            run_game = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if is_clicked_on_constructor():
                new_cursor = get_type_of_ship()
                if new_cursor == cfg.cursor:
                    cfg.rotate = not cfg.rotate
                cfg.cursor = new_cursor
                click_on_constructor()
            else:
                cfg.cursor = is_clicked_on_grid(grid)


def is_clicked_on_grid(grid):
    if cursor_collider(grid):
        pygame.mouse.set_cursor(cfg.cursor_normal)
        mouse_position = pygame.mouse.get_pos() 
        position = [mouse_position[0], mouse_position[1]]
        grid_start = grid.get_grid_start_position()
        position[0] -= grid_start[0]
        position[1] -= grid_start[1]
        
        element = int((position[0] - position[0] % cfg.photo_size[0]) / cfg.photo_size[0])
        line = int((position[1] - position[1] % cfg.photo_size[0]) / cfg.photo_size[0])


        array_of_cells = []
        if cfg.rotate:
            for x in range(cfg.cursor):
                array_of_cells.append([line + x, element])
            grid.set_ship(array_of_cells)
        else:
            for x in range(cfg.cursor):
                array_of_cells.append([line, element + x])
            grid.set_ship(array_of_cells)

    else:
        pygame.mouse.set_cursor(cfg.cursor_normal)
    cfg.rotate = False
    return 0


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
            if element["modification"] == "clear":
                screen.blit(cfg.space, (w, h))
            elif element["modification"] == "miss":
                screen.blit(cfg.miss, (w, h))
            elif element["modification"] == "ship":
                screen.blit(cfg.ship, (w, h))
            elif element["modification"] == "damaged":
                screen.blit(cfg.damaged, (w, h))
            elif element["modification"] == "killed":
                screen.blit(cfg.killed, (w, h))
            w += cfg.photo_size[0]
        w = w_start_func
        h += cfg.photo_size[1]
    pygame.draw.rect(screen, pygame.Color("gray"),
                     (w_start_func, h_start_func, cfg.photo_size[0] * 10, cfg.photo_size[1] * 10), 1)


def draw_one_grid_with_symbols(grid, w_start, h_start):
    draw_symbols(*grid.get_symbols_position())
    draw_numbers(*grid.get_number_position())
    draw_grid(grid, *grid.get_grid_start_position())


def set_positions(grid, w_start, h_start):
    grid.set_symbols_position(w_start, h_start)
    grid.set_numbers_position(w_start, h_start + cfg.photo_size[0])
    grid.set_grid_start_position(w_start + cfg.photo_size[0], h_start + cfg.photo_size[0])
    grid.set_grid_end_position(w_start + cfg.photo_size[0] + cfg.photo_size[0] * 10,
                               h_start + cfg.photo_size[0] + cfg.photo_size[1] * 10)


def cursor_collider(grid):
    mouse_position = pygame.mouse.get_pos()
    start_position = grid.get_grid_start_position()
    end_position = grid.get_grid_end_position()
    if start_position[0] <= mouse_position[0] < end_position[0] and \
            start_position[1] <= mouse_position[1] < end_position[1]:
        return True
    else:
        return False


def draw_constructor():
    x, y = cfg.constructor_position[0], cfg.constructor_position[1]
    for type_of_ship in cfg.types_of_ships:
        for length in range(type_of_ship):
            screen.blit(cfg.ship, (x, y))
            x += cfg.photo_size[0]
        x = cfg.constructor_position[0]
        y += cfg.photo_size[0] + 10

    # y = cfg.constructor_position[1] + 4 * (cfg.photo_size[0] + 10)
    # x = cfg.constructor_position[0]
    # screen.blit(cfg.killed, (x, y))

    if cfg.cursor != 0:
        try:
            mouse_position = pygame.mouse.get_pos()
            x, y = mouse_position[0] - cfg.photo_size[0] * 4 / 10, mouse_position[1] - cfg.photo_size[0] * 4 / 10
            for cell in range(cfg.cursor):
                screen.blit(cfg.ship, (x, y))
                if cfg.rotate:
                    y += cfg.photo_size[0]
                else:
                    x += cfg.photo_size[0]
        except:
            pass

def is_clicked_on_constructor():
    x, y = cfg.constructor_position[0], cfg.constructor_position[1]
    mouse_position = pygame.mouse.get_pos()
    for type_of_ship in cfg.types_of_ships:
        y_ship = y + (type_of_ship - 1) * (cfg.photo_size[0] + 10)
        if x <= mouse_position[0] < x + type_of_ship * cfg.photo_size[0] and \
                y_ship <= mouse_position[1] < y_ship + cfg.photo_size[0]:
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            return True
    return False


def get_type_of_ship():
    x, y = cfg.constructor_position[0], cfg.constructor_position[1]
    mouse_position = pygame.mouse.get_pos()
    for type_of_ship in cfg.types_of_ships:
        y_ship = y + (type_of_ship - 1) * (cfg.photo_size[0] + 10)
        if x <= mouse_position[0] < x + type_of_ship * cfg.photo_size[0] and \
                y_ship <= mouse_position[1] < y_ship + cfg.photo_size[0]:
            # pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            return type_of_ship


def click_on_constructor():
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)


def main():
    pygame.init()
    player_1, player_2 = 0, 1
    grid_1 = Grid(player_1, player_2)
    set_positions(grid_1, 10, 10)
    grid_2 = Grid(player_2, player_1)

    global run_game
    while run_game:
        events(grid_1)

        screen.fill(pygame.Color("white"))

        draw_one_grid_with_symbols(grid_1, 10, 10)
        # print(cursor_collider(grid_1))
        # draw_one_grid_with_symbols(grid_1, 250, 10)
        # draw_one_grid_with_symbols(grid_2, 10, 320)
        # draw_one_grid_with_symbols(grid_2, 250, 320)

        draw_constructor()

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
