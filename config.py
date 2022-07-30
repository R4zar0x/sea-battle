import pygame

screen_width, screen_height = 800, 600  # 924, 693; 1366, 768; 1920, 1080; GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode((screen_width, screen_height))  # pygame.FULLSCREEN
screen.fill(pygame.Color("white"))

photo_size = (20, 20)
clock = pygame.time.Clock()
fps = 30
font = pygame.font.Font(None, photo_size[0])

space = pygame.transform.scale(pygame.image.load("Пустое место.png"), (photo_size[0], photo_size[1]))
miss = pygame.transform.scale(pygame.image.load("Мимо.png"), (photo_size[0], photo_size[1]))
ship = pygame.transform.scale(pygame.image.load("Корабль.png"), (photo_size[0], photo_size[1]))
damaged = pygame.transform.scale(pygame.image.load("Подбит.png"), (photo_size[0], photo_size[1]))
killed = pygame.transform.scale(pygame.image.load("Убит.png"), (photo_size[0], photo_size[1]))

symbols = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
start_width, start_height = 10, 30

grids = []
