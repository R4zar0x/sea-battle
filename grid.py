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

    def add_ship(self, ship_id, position, direction):
        
    

        pass

    def mouse_in_field(self):
        mouse_positions = pygame.mouse.get_pos()

        if self.position_x <= mouse_positions[0] < self.position_x + 10 * self.grid_scale and \
                self.position_y <= mouse_positions[1] < self.position_y + 10 * self.grid_scale:
            return True
        else:
            return False

    def mouse_clik(self):
        if self.mouse_in_field():
            pressed_keys_on_mouse = pygame.mouse.get_pressed()
            if pressed_keys_on_mouse[0]:

                mouse_position = pygame.mouse.get_pos()

                element = int((mouse_position[0] - mouse_position[0] % self.grid_scale) / self.grid_scale) - 1

                print(element)
                line = int((mouse_position[1] - mouse_position[1] % self.grid_scale) / self.grid_scale) - 1

                if self.field[line][element] != 0:

                    id_ship = self.field[line][element] - 1
                    ship = self.ships[id_ship]
                    direction_of_ship = ship.get_direction()
                    coordinates = ship.get_coordinates()

                    unit = 0

                    if direction_of_ship == 0 or direction_of_ship == 2:
                        unit = abs(element - coordinates[1])
                    elif direction_of_ship == 1 or direction_of_ship == 3:
                        unit = abs(line - coordinates[0])

                    if ship.is_alive(unit):
                        ship.hit(unit)

    def get_field(self):
        return self.field

    def set_scale(self, new_scale):
        self.grid_scale = new_scale

    def set_grid_color(self, new_color):
        self.grid_color = new_color
