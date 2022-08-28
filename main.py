from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from config import screen, fps, clock

from input_box import Box
from button import Button
from local_grid import Grid

import config as cfg

import constructor
import menu
import game
import end


pygame.init()

# при нажатии f поле авоматически заполняется сохраненным


def show_game_mode():
    print(cfg.game_mode)


def main():
    player_1, player_2 = 0, 1
    grid_1 = Grid(player_1, player_2, "Invoker")
    grid_2 = Grid(player_2, player_1, "Axe")
    button = Button(300, 180, 100, 50)
    button.set_text("Next player")
    button.set_function(menu.button_next, grid_1)

    box = Box(30, 260, 140, 32)
    box.set_text(grid_1.get_player_name())

    cfg.game_mode = cfg.game_mods[0]

    while cfg.menu and cfg.run:
        # events
        menu.events(grid_1, button, box, 300, 50)

        button.set_button_color(menu.button_color(grid_1))
        button.set_text_color(menu.button_color(grid_1))

        box.update()

        # draw functions
        # screen.fill(pygame.Color("white"))
        screen.blit(cfg.background, (0, 0))

        grid_1.draw_grid(screen, 10, 10, player=0)

        constructor.draw_constructor(grid_1, 300, 50)
        button.draw_button(screen)
        box.draw(screen)

        menu.text_draw(screen, grid_1, 30, 240)

        clock.tick(fps)
        pygame.display.flip()

    grid_1.set_player_name(box.get_text())
    box.set_text(grid_2.get_player_name())

    button.set_text("Start game")
    button.set_function(menu.button_next, grid_2)

    cfg.menu = True
    while cfg.menu and cfg.run:
        # events
        menu.events(grid_2, button, box, 300, 300)

        button.set_button_color(menu.button_color(grid_2))
        button.set_text_color(menu.button_color(grid_2))

        box.update()

        # draw functions
        # screen.fill(pygame.Color("white"))
        screen.blit(cfg.background, (0, 0))

        grid_2.draw_grid(screen, 10, 10, player=1)

        constructor.draw_constructor(grid_2, 300, 50)
        button.draw_button(screen)
        box.draw(screen)

        clock.tick(fps)
        pygame.display.flip()

    grid_2.set_player_name(box.get_text())

    cfg.game_mode = cfg.game_mods[2]
    cfg.game = True
    while cfg.game and cfg.run:
        # screen.fill(pygame.Color("white"))
        screen.blit(cfg.background, (0, 0))

        grid_1.draw_grid(screen, 10, 10, player=0)
        grid_2.draw_grid(screen, 10, 300, player=1)
        grid_2.draw_grid(screen, 250, 10, player=0)
        grid_1.draw_grid(screen, 250, 300, player=1)

        game.events([grid_1, grid_2])

        clock.tick(fps)
        pygame.display.flip()

    button = Button(cfg.screen_width / 2 - 50, 200, 100, 50)
    button.set_text("Exit")
    button.set_button_color(pygame.Color("lightblue"))
    button.set_text_color(pygame.Color("lightblue"))

    button.set_function(end.button_end, None)

    cfg.end = True
    while cfg.end and cfg.run:
        end.events(button)

        # screen.fill(pygame.Color("white"))
        screen.blit(cfg.background, (0, 0))

        end.draw_text(screen,
                      (cfg.screen_width / 2), 150,
                      f"{cfg.winner} win")

        button.draw_button(screen)

        clock.tick(fps)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
