import pygame
import config as cfg


class Button:

    def __init__(self, button_x, button_y, button_width, button_height):

        self.button_width = button_width
        self.button_height = button_height
        self.button_x = button_x
        self.button_y = button_y

        self.arguments = None
        self.function = None
        self.text = ""

        self.button_color = pygame.Color(40, 10, 80)
        self.text_color = pygame.Color(40, 10, 80)

    def button_click(self):
        if self.arguments is None:
            self.function()
        else:
            self.function(self.arguments)

    def draw_button(self, surface):
        pygame.draw.rect(surface, self.button_color,
                         (self.button_x, self.button_y,
                          self.button_width, self.button_height), 1)
        text = cfg.font.render(self.text, cfg.antialias, self.text_color)
        position = (self.button_x + self.button_width / 2 - text.get_width() / 2,
                    self.button_y + self.button_height / 2 - text.get_height() / 2)
        surface.blit(text, position)

    def is_mouse_on_button(self):
        mouse_position = pygame.mouse.get_pos()
        if self.button_x < mouse_position[0] < self.button_x + self.button_width and \
                self.button_y < mouse_position[1] < self.button_y + self.button_height:
            return True
        else:
            return False

    def set_text(self, text):
        self.text = text

    def set_button_color(self, color):
        self.button_color = color

    def set_text_color(self, color):
        self.text_color = color

    def set_function(self, function, argument=None):
        self.function = function
        self.arguments = argument
