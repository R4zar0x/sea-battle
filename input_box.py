import pygame


class Box:

    def __init__(self, x, y, w, h, text=''):

        self.color_inactive = pygame.Color('darkgray')      # lightskyblue3
        self.color_active = pygame.Color('lightgray')         # dodgerblue2
        self.font = pygame.font.Font(None, 32)
        self.max_count_char_in_line = 32

        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE or event.key == pygame.K_TAB:
                    self.active = not self.active
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < self.max_count_char_in_line:
                    self.text += event.unicode

        self.color = self.color_active if self.active else self.color_inactive

        self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def set_color_active(self, color):
        self.color_active = color

    def set_color_inactive(self, color):
        self.color_inactive = color

    def set_font(self, font):
        self.font = font

    def set_text(self, text):
        self.text = text

    def set_max_count_char_in_line(self, max_count):
        self.max_count_char_in_line = max_count

    def get_text(self):
        return self.text

    def get_active(self):
        return self.active
