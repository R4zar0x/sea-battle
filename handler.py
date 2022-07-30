import pygame

pygame.init()


class Grid:

    def __init__(self, player, opponent):

        self.player = player
        self.opponent = opponent

        self.ships = []
        self.field = []
        for line in range(10):
            self.field.append([])
            for element in range(10):
                # miss, clear, ship, damaged, killed - modifications
                self.field[line].append({"index": line * 10 + element,
                                         "modification": "clear",
                                         "vision": False,
                                         "ship_id": 0})

    def set_ship(self, ship_id):
        pass

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