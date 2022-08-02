import pygame
import config as cfg


class Grid:

    def __init__(self, player, opponent, x_set, y_set, cell_size=20):

        self.cell_size = cell_size
        self.player = player
        self.opponent = opponent

        self.position_start = [x_set, y_set]
        self.grid_position_start = [x_set + cell_size, y_set + cell_size]
        self.position_end = [x_set + 11 * cell_size, y_set + 11 * cell_size]

        # alive, killed - modifications
        self.ships = []     # [[modification, cell_id, cell_id], [modification, cell_id]]
        self.field = []
        for line in range(10):
            self.field.append([])
            for element in range(10):
                # miss, clear, ship, damaged, killed - modifications
                self.field[line].append({"index": line * 10 + element,
                                         "modification": "clear",
                                         "vision": False,
                                         "ship_id": 0})

    def draw_grid(self, screen):
        width, height = self.grid_position_start[0], self.grid_position_start[1]
        for line in self.field:
            for element in line:
                if element["modification"] == "clear":
                    screen.blit(cfg.space, (width, height))
                elif element["modification"] == "miss":
                    screen.blit(cfg.miss, (width, height))
                elif element["modification"] == "ship":
                    screen.blit(cfg.ship, (width, height))
                elif element["modification"] == "damaged":
                    screen.blit(cfg.damaged, (width, height))
                elif element["modification"] == "killed":
                    screen.blit(cfg.killed, (width, height))
                width += self.cell_size
            width = self.grid_position_start[0]
            height += self.cell_size
        pygame.draw.rect(screen, pygame.Color("gray"),
                         (self.grid_position_start[0], self.grid_position_start[1], self.cell_size * 10, self.cell_size * 10), 1)

        width, height = self.position_start[0], self.position_start[1] + self.cell_size / 10
        for symbol in cfg.symbols:
            text = cfg.font.render(symbol, cfg.antialias, pygame.Color("black"))
            screen.blit(text, (width + 6 + self.cell_size, height))
            width += self.cell_size

        width, height = self.position_start[0] + self.cell_size / 4, self.position_start[1] + self.cell_size
        for i in range(10):
            text = cfg.font.render(str(i + 1), cfg.antialias, pygame.Color("black"))
            screen.blit(text, (width - (3 if i == 9 else 0), height + 3))
            height += cfg.photo_size[0]

    def cursor_in_grid(self):
        mouse_position = pygame.mouse.get_pos()

        if self.grid_position_start[0] <= mouse_position[0] < self.position_end[0] and \
                self.grid_position_start[1] <= mouse_position[1] < self.position_end[1]:
            return True
        return False

    def set_ship(self, cell_list):       # [[row, td]]
        self.ships.append(['alive'])
        for cell in cell_list:
            cell_id = cell[0] * 10 + cell[1]
            self.ships[len(self.ships) - 1].append(cell_id)
            self.field[cell[0]][cell[1]]["modification"] = "ship"
            self.field[cell[0]][cell[1]]["ship_id"] = len(self.ships) - 1

    def set_field(self, field):
        self.field = field

    def get_position_end(self):
        return self.position_end

    def get_position_start(self):
        return self.position_start

    def get_field(self):
        return self.field


class Ship:

    def __init__(self, ship_id, cells_list, length):
        self.id = ship_id
        self.cells_list = cells_list
        self.length = length
