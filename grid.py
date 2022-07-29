import pygame

pygame.init()

letters = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И"]


class Grid:

    def __init__(self, player, position_x, position_y, player_color,
                 grid_color=pygame.Color("lightgray"),
                 grid_scale=20):

        self.player = player
        self.position_x = position_x
        self.position_y = position_y
        self.player_color = player_color
        self.ships = []

        self.grid_color = grid_color
        self.grid_scale = grid_scale

        self.field = []
        for line in range(10):
            self.field.append([])
            for element in range(10):
                self.field[line].append(0)

    def draw_grid(self, surface, font):

        for horizontal in range(10):
            for vertical in range(10):
                new_x = self.position_x + horizontal * self.grid_scale
                new_y = self.position_y + vertical * self.grid_scale

                color = self.grid_color if not self.field[horizontal][vertical] else self.player_color

                pygame.draw.rect(surface, color, (new_x, new_y, self.grid_scale, self.grid_scale), 1)

    def add_ship(self, ship_id, ship_x, ship_y, direction):

        position_x = self.position_x + ship_x
        position_y = self.position_y + ship_y

        if direction == 0:

            for square in range(ship_id):
                square_x = position_x +
                square_y = position_y +

