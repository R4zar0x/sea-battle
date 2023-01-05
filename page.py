import pygame
import config as cfg

class Page:
    def __init__(self, rooms, rect_positions: tuple):
        self.rect = pygame.Rect(rect_positions)
        self.all_rooms = rooms
        self.page = 0

        self.rooms_on_page = []

        for rooms in range(cfg.max_rooms_on_page):
            room_positions = (10 + rect_positions[0], 
            10 + rect_positions[1] + 30 * rooms, 
            rect_positions[2] - 20, 25)
            self.rooms_on_page.append(pygame.Rect(room_positions))

    def handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_positions = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_positions):
                condition = len(self.all_rooms) - self.page * cfg.max_rooms_on_page 
                active_rooms = cfg.max_rooms_on_page if condition >= cfg.max_rooms_on_page else condition
                for i in range(active_rooms):
                    if self.rooms_on_page[i].collidepoint(mouse_positions):
                        # реакция на нажатие на комнату
                        print("click on " + self.all_rooms[self.page * cfg.max_rooms_on_page + i]["room_name"])

    def draw(self, surface: pygame.Surface, color: tuple = pygame.Color("darkgreen")):
        background_pos = (self.rect[0] - 10, self.rect[1] - 10, self.rect[2] + 20, self.rect[3] + 70)
        pygame.draw.rect(surface, pygame.Color("white"), background_pos, border_radius=5)
        pygame.draw.rect(surface, pygame.Color("gray"), self.rect, 2, border_radius=5)

        condition = len(self.all_rooms) - self.page * cfg.max_rooms_on_page 
        active_rooms = cfg.max_rooms_on_page if condition >= cfg.max_rooms_on_page else condition
        for i in range(active_rooms):
            rect = self.rooms_on_page[i]
            txt = cfg.font.render(self.all_rooms[self.page * cfg.max_rooms_on_page + i]["room_name"], True, color)
        
            pygame.draw.rect(surface, color, rect, 2, border_radius=5)
            surface.blit(txt, (rect[0] + 5, rect[1] + 5))

    def next_page(self):
        if self.page + 1 < len(self.all_rooms) // cfg.max_rooms_on_page + 1:
            self.page += 1
    
    def prev_page(self):
        if self.page - 1 >= 0:
            self.page -= 1
