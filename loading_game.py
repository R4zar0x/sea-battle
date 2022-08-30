import pygame

import config as cfg


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if cfg.load:
                cfg.load = False
                cfg.run = False


def draw(surface):
    if cfg.developers_damping:
        developers_damping(surface)

    elif cfg.developers_occurrence:
        developers_occurrence(surface)

    elif cfg.background_damping:
        background_damping(surface)


def developers_damping(surface):
    text = ["Developers:", "tegic", "R4zar0x"]

    y = 200
    for line in text:
        txt = cfg.end_font.render(line, True, pygame.Color("white"))
        txt.set_alpha(cfg.alpha)
        surface.blit(txt, ((cfg.screen_width - txt.get_width()) / 2, y))

        y += 30

    if cfg.alpha < 255:
        cfg.alpha += cfg.animations_frames / (cfg.fps * cfg.animations_time / 3)
    if cfg.alpha >= 255:
        cfg.alpha = 255
        cfg.developers_damping = False
        cfg.developers_occurrence = True


def developers_occurrence(surface):
    text = ["Developers:", "tegic", "R4zar0x"]

    y = 200
    for line in text:
        txt = cfg.end_font.render(line, True, pygame.Color("white"))
        txt.set_alpha(cfg.alpha)
        surface.blit(txt, ((cfg.screen_width - txt.get_width()) / 2, y))

        y += 30

    if cfg.alpha > 0:
        cfg.alpha -= cfg.animations_frames / (cfg.fps * cfg.animations_time / 3)
    if cfg.alpha <= 0:
        cfg.alpha = 0
        cfg.developers_occurrence = False
        cfg.background_damping = True


def background_damping(surface):
    image = cfg.background

    image.set_alpha(cfg.alpha)

    surface.blit(image, (0, 0))

    if cfg.alpha < 255:
        cfg.alpha += cfg.animations_frames / (cfg.fps * cfg.animations_time / 3)
    if cfg.alpha >= 255:
        cfg.alpha = 255
        cfg.background_damping = False
        cfg.load = False
