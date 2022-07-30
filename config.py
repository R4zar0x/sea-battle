import pygame

screen_width, screen_height = 400, 600  # 924, 693; 1366, 768; 1920, 1080; GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode((screen_height, screen_width))  # pygame.FULLSCREEN
screen.fill(pygame.Color("white"))

clock = pygame.time.Clock()
fps = 30
font = pygame.font.Font(None, 27)
