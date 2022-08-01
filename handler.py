import pygame

pygame.init()


class Grid:

    def __init__(self, player, opponent):

        self.player = player
        self.opponent = opponent
        self.symbols_start_position = []
        self.numbers_start_position = []
        self.grid_start_position = []
        self.grid_end_position = []

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

    def set_ship(self, cell_list):  #[[row, td]]
        self.ships.append(['alive'])
        for cell in cell_list:
            cell_id = cell[0] * 10 + cell[1]
            self.ships[len(self.ships) - 1].append(cell_id)
            self.field[cell[0]][cell[1]]["modification"] = "ship"
            self.field[cell[0]][cell[1]]["ship_id"] = len(self.ships) - 1

    def set_symbols_position(self, w, h):
        self.symbols_start_position = [w, h]

    def get_symbols_position(self):
        return self.symbols_start_position

    def set_numbers_position(self, w, h):
        self.numbers_start_position = [w, h]

    def get_number_position(self):
        return self.numbers_start_position

    def set_grid_start_position(self, w, h):
        self.grid_start_position = [w, h]

    def get_grid_start_position(self):
        return self.grid_start_position

    def set_grid_end_position(self, w, h):
        self.grid_end_position = [w, h]

    def get_grid_end_position(self):
        return self.grid_end_position

    def hit_ship(self):
        pass

    def kill_ship(self):
        pass

    def miss(self):
        pass

    def get_field(self):
        return self.field


class Ship:

    def __init__(self, ship_id, cells_list, length):
        self.id = ship_id
        self.cells_list = cells_list
        self.length = length



def main():
    pass

if __name__ == "__main__":
    main()