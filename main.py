from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

from button import Button
from local_grid import Grid
import config as cfg
from config import screen, fps, clock
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
    grid_1 = Grid(player_1, player_2, "Alex")
    grid_2 = Grid(player_2, player_1, "ultraildo")
    button = Button(300, 200, 100, 50)
    button.set_text("Next player")
    button.set_function(menu.button_next, grid_1)

    cfg.game_mode = cfg.game_mods[0]

    while cfg.menu and cfg.run:
        menu.events(grid_1, button, 300, 50)

        button.set_button_color(menu.button_color(grid_1))
        button.set_text_color(menu.button_color(grid_1))

        # screen.fill(pygame.Color("white"))
        screen.blit(cfg.background, (0, 0))

        grid_1.draw_grid(screen, 10, 10, player=0)

        constructor.draw_constructor(grid_1, 300, 50)

        button.draw_button(screen)

        clock.tick(fps)
        pygame.display.flip()

    button.set_text("Start game")
    button.set_function(menu.button_next, grid_2)

    cfg.menu = True
    while cfg.menu and cfg.run:
        menu.events(grid_2, button, 300, 300)

        button.set_button_color(menu.button_color(grid_2))
        button.set_text_color(menu.button_color(grid_2))

        # screen.fill(pygame.Color("white"))
        screen.blit(cfg.background, (0, 0))

        grid_2.draw_grid(screen, 10, 250, player=1)

        constructor.draw_constructor(grid_2, 300, 300)

        button.draw_button(screen)

        clock.tick(fps)
        pygame.display.flip()

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

    button = Button(200, 200, 100, 50)
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
                      ((cfg.screen_width / 2) - (len(cfg.winner) / 2) * 17, 150),
                      f"{cfg.winner} win")

        button.draw_button(screen)

        clock.tick(fps)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
