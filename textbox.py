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

    def call_action_if_clicked(self, clicked_point, item_view_window, equipment, board, task_manager, stm):
        if self.left_top[0] <= clicked_point[0] <= self.right_bottom[0] and self.left_top[1] <= clicked_point[1] <= self.right_bottom[1]:
            if self.sentence == 'Take this item':
                item_view_window.current_item.is_active = 0
                equipment.add_item_to_equipment(item_view_window.current_item)
                item_to_remove = item_view_window.current_item
                item_view_window.hide_item()
                board.remove_item_from_board(item_to_remove)
            elif self.sentence == 'I don\'t need it' or self.sentence == 'Exit':
                if item_view_window.current_item.name == "Lock":
                    task_manager.disable_flag("LOCK_ACTIVATED")
                item_view_window.current_item.is_active = 0
                item_view_window.hide_item()
            elif self.sentence == 'You can use {}'.format(item_view_window.current_item.interact_with):
                item_view_window.hide_item()
                equipment.remove_item()
                task_manager.enable_task_action("open_secret_box")
            elif self.sentence == 'You can repair the cube':
                item_view_window.hide_item()
                stm.write_sth("repair")
                task_manager.enable_task_action("repair_box")
            elif self.sentence == 'Accept the entered code':
                if stm.write_sth("key") == "OK":
                    item_view_window.hide_item()
                    task_manager.enable_task_action("unlock_house_door")
            else:
                print('No action with this textbox')