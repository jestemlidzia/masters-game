import pygame, os, json

class TextBox(object):
    def __init__(self, screen, sentence, font_color, font_name, font_size, center):
        self.screen = screen
        self.sentence = sentence
        self.font_color = font_color
        self.font_name = font_name
        self.font_size = font_size
        self.center = center

        self.font = pygame.font.Font(os.path.join('font', self.font_name), self.font_size)
    
    def display_text(self, new_sentence = ''):
        if new_sentence != '':
            self.text = self.font.render(new_sentence, True, self.font_color)
            self.textRect = self.text.get_rect()
            self.textRect.center = self.center
        else:
            self.text = self.font.render(self.sentence, True, self.font_color)
            self.textRect = self.text.get_rect()
            self.textRect.center = self.center

        self.screen.blit(self.text, self.textRect)