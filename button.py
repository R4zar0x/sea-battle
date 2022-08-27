import pygame
import config as cfg


class Button:

    def __init__(self, button_x, button_y, button_width, button_height):

        self.button_size = [button_width, button_height]
        self.button_position = [button_x, button_y]
        self.text_position = [button_x + button_width / 2, button_y + (button_height - cfg.photo_size[0] / 1.5) / 2]

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
                         (self.button_position[0], self.button_position[1],
                          self.button_size[0], self.button_size[1]), 1)
        text = cfg.font.render(self.text, cfg.antialias, self.text_color)
        surface.blit(text, (self.text_position[0], self.text_position[1]))

    def is_mouse_on_button(self):
        mouse_position = pygame.mouse.get_pos()
        if self.button_position[0] < mouse_position[0] < self.button_position[0] + self.button_size[0] and \
                self.button_position[1] < mouse_position[1] < self.button_position[1] + self.button_size[1]:
            return True
        else:
            return False

    def set_text(self, text):
        self.text = text
        middle_position = (self.button_size[0] - len(self.text) * cfg.photo_size[0] / 3) / 2
        self.text_position[0] = self.button_position[0] + middle_position

    def set_button_color(self, color):
        self.button_color = color

    def set_text_color(self, color):
        self.text_color = color

    def set_function(self, function, argument):
        self.function = function
        self.arguments = argument
