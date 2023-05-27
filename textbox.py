import pygame, os, json

class TextBox(object):
    def __init__(self, screen, sentence, font_color, font_name, font_size, center, left_top, right_bottom):
        self.screen = screen
        self.sentence = sentence
        self.font_color = font_color
        self.font_name = font_name
        self.font_size = font_size
        self.center = center
        self.left_top = left_top
        self.right_bottom = right_bottom

        self.font = pygame.font.Font(os.path.join('font', self.font_name), self.font_size)
    
    def display_text(self, new_sentence = ''):
        if new_sentence != '':
            self.sentence = new_sentence
            self.text = self.font.render(new_sentence, True, self.font_color)
            self.textRect = self.text.get_rect()
            self.textRect.center = self.center
        else:
            self.text = self.font.render(self.sentence, True, self.font_color)
            self.textRect = self.text.get_rect()
            self.textRect.center = self.center

        self.screen.blit(self.text, self.textRect)

    def call_action_if_clicked(self, clicked_point, item_view_window, equipment, board):
        if self.left_top[0] <= clicked_point[0] <= self.right_bottom[0] and self.left_top[1] <= clicked_point[1] <= self.right_bottom[1]:
            if self.sentence == 'Take this item':
                item_view_window.current_item.is_active = 0
                equipment.add_item_to_equipment(item_view_window.current_item)
                item_to_remove = item_view_window.current_item
                item_view_window.hide_item()
                board.remove_item_from_board(item_to_remove)
            elif self.sentence == 'I don\'t need it' or self.sentence == 'Exit':
                item_view_window.current_item.is_active = 0
                item_view_window.hide_item()
            elif self.sentence == 'You can use XXX':
                print()
            else:
                print('No action with this textbox')

