import pygame
import config as cfg
from pprint import pprint


class Grid:

    def __init__(self, player, opponent, cell_size=20):

        self.cell_size = cell_size
        self.player = player
        self.opponent = opponent

        self.position_start = []
        self.grid_position_start = []
        self.position_end = []

        self.possible_count_of_ships = [4, 3, 2, 1]

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

    def draw_grid(self, screen, x_set, y_set, player):
        self.position_start = [x_set, y_set]
        self.grid_position_start = [x_set + self.cell_size, y_set + self.cell_size]
        self.position_end = [x_set + 11 * self.cell_size, y_set + 11 * self.cell_size]

        width, height = self.grid_position_start[0], self.grid_position_start[1]
        for line in self.field:
            for element in line:
                if player != self.player and player == self.opponent:
                    if not element["vision"]:
                        screen.blit(cfg.space, (width, height))
                    else:
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
                elif player == self.player and player != self.opponent:
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

    def is_free_space_for_ship(self, rotate, ship_position_line, ship_position_element):
        field = self.get_field()
        if rotate:
            for line in range(cfg.cursor + 2):
                for element in range(3):
                    cell_line = ship_position_line - 1 + line
                    cell_element = ship_position_element - 1 + element
                    if 0 <= cell_line < 10 and 0 <= cell_element < 10:
                        cell = field[cell_line][cell_element]
                        if cell["modification"] == "ship":
                            return False
        else:
            for line in range(3):
                for element in range(cfg.cursor + 2):
                    cell_line = ship_position_line - 1 + line
                    cell_element = ship_position_element - 1 + element
                    if 0 <= cell_line < 10 and 0 <= cell_element < 10:
                        cell = field[cell_line][cell_element]
                        if cell["modification"] == "ship":
                            return False
        return True

    def is_count_of_ships_null(self):
        for count in self.possible_count_of_ships:
            if count != 0:
                return False
        return True

    def set_positions(self, x_set, y_set):
        self.position_start = [x_set, y_set]
        self.grid_position_start = [x_set + self.cell_size, y_set + self.cell_size]
        self.position_end = [x_set + 11 * self.cell_size, y_set + 11 * self.cell_size]

    def set_ship(self, cell_list):       # [[row, td]]
        self.possible_count_of_ships[len(cell_list) - 1] -= 1

        self.ships.append(['alive'])
        for cell in cell_list:
            cell_id = cell[0] * 10 + cell[1]
            self.ships[len(self.ships) - 1].append(cell_id)
            self.field[cell[0]][cell[1]]["modification"] = "ship"
            self.field[cell[0]][cell[1]]["ship_id"] = len(self.ships) - 1

    def set_miss_modification_around_of_killed_ship(self, ship_id):
        ship = self.ships[ship_id]
        # print(ship)
        # pprint(self.ships)
        field = self.field
        for i in range(len(ship) - 1):
            cells_around_that_cell = []  # [line, element]
            cell_id = ship[i + 1]
            line = int(cell_id / 10)
            element = int(cell_id % 10)
            if element > 0:
                cells_around_that_cell.append([line, element - 1])
            if line > 0 and element > 0:
                cells_around_that_cell.append([line - 1, element - 1])
            if line < 9 and element > 0:
                cells_around_that_cell.append([line + 1, element - 1])
            if line < 9:
                cells_around_that_cell.append([line + 1, element])
            if line > 0:
                cells_around_that_cell.append([line - 1, element])
            if line > 0 and element < 9:
                cells_around_that_cell.append([line - 1, element + 1])
            if element < 9:
                cells_around_that_cell.append([line, element + 1])
            if line < 9 and element < 9:
                cells_around_that_cell.append([line + 1, element + 1])
            for cell_near in cells_around_that_cell:
                line, element = cell_near[0], cell_near[1]
                if field[line][element]["modification"] == "clear":
                    self.field[line][element]["modification"] = "miss"
                    self.field[line][element]["vision"] = True

    def get_cell_under_cursor(self):
        mouse = pygame.mouse.get_pos()
        mouse_position = [mouse[0], mouse[1]]
        grid_start_position = self.grid_position_start

        x = mouse_position[0] - grid_start_position[0]
        y = mouse_position[1] - grid_start_position[1]

        element = int((x - x % self.cell_size) / self.cell_size)
        line = int((y - y % self.cell_size) / self.cell_size)
        return [line, element]

    def get_position_end(self):
        return self.position_end

    def get_position_start(self):
        return self.position_start

    def get_possible_count_of_ships(self):
        return self.possible_count_of_ships

    def get_field(self):
        return self.field

    def get_player(self):
        return self.player
    
    def what_ship_id(self, line, element):
        cell_id = str(line) + str(element)
        id = 0
        for ship in self.ships:
            for i in range(len(ship) - 1):
                if int(ship[i + 1]) == int(cell_id):
                    ship_id = id
                    return ship_id
            id += 1

    def damage_ship(self, line, element):
        self.get_field()[line][element]["modification"] = "damaged"

    def kill_ship(self, ship_id):
        ship = self.ships[ship_id]
        self.ships[ship_id][0] = 'killed'
        cells_line_and_element_list = []
        for i in range(len(ship) - 1):
            cell_id = ship[i + 1]
            # cells_line_and_element_list.append([int(cell_id / 10), int(cell_id - cell_id / 10)])
            line = int(cell_id / 10)
            element = int(cell_id % 10)
            self.get_field()[line][element]["modification"] = "killed"
        self.set_miss_modification_around_of_killed_ship(ship_id)

    def click_on_grid(self, line, element):
        # for game
        if self.field[line][element]["modification"] == "clear":
            self.field[line][element]["modification"] = "miss"
        elif self.field[line][element]["modification"] == "ship":
            ship_id = self.what_ship_id(line, element)
            # print(str(self.ships) + "********" + str(ship_id))
            if self.is_ship_will_die_now(ship_id):
                self.kill_ship(ship_id)
            else:
                self.damage_ship(line, element)
        self.field[line][element]["vision"] = True

    def is_ship_will_die_now(self, ship_id):
        count_of_not_damaged_parts_of_ship = 0
        ship = self.ships[ship_id]
        cells_id_list = []
        for i in range(len(ship) - 1):
            cells_id_list.append(ship[i + 1])
        for cell_id in cells_id_list:
            cell = self.get_field()[int(cell_id / 10)][int(cell_id % 10)]
            if cell["modification"] == "ship":
                count_of_not_damaged_parts_of_ship += 1
        count_of_damaged_parts_of_ship = len(ship) - count_of_not_damaged_parts_of_ship
        # print(str(count_of_damaged_parts_of_ship) + " " + str(len(ship) - 1))
        if count_of_damaged_parts_of_ship == len(ship) - 1: # without modification and 1 cell
            return True
        else:
            return False


class Ship:

    def __init__(self, ship_id, cells_list, length):
        self.id = ship_id
        self.cells_list = cells_list
        self.length = length
