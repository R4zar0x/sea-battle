import pygame

import config as cfg


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.load:
                cfg.load = False
                cfg.run = False


def draw_developers(surface):

    if cfg.draw_developers_before:
        text = ["Developers:", "tegic", "R4zar0x"]

        y = 200
        for line in text:
            txt = cfg.end_font.render(line, True, pygame.Color("white"))
            txt.set_alpha(cfg.alpha)
            surface.blit(txt, ((cfg.screen_width - txt.get_width()) / 2, y))

            y += 30

        if cfg.alpha < 255:
            cfg.alpha += 1
        if cfg.alpha == 255:
            cfg.draw_developers_before = False
            cfg.draw_developers_after = True

    elif cfg.draw_developers_after:
        text = ["Developers:", "tegic", "R4zar0x"]

        y = 200
        for line in text:
            txt = cfg.end_font.render(line, True, pygame.Color("white"))
            txt.set_alpha(cfg.alpha)
            surface.blit(txt, ((cfg.screen_width - txt.get_width()) / 2, y))

            y += 30

        if cfg.alpha > 0:
            cfg.alpha -= 1
        if cfg.alpha == 0:
            cfg.draw_developers_after = False
            cfg.draw_background = True
    elif cfg.draw_background:
        image = cfg.background

        image.set_alpha(cfg.alpha)

        surface.blit(image, (0, 0))

        if cfg.alpha < 255:
            cfg.alpha += 1
        if cfg.alpha == 255:
            cfg.load = False
