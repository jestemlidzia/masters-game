import pygame
import os

class TextBox:
    FONT_PATH = 'font'
    
    def __init__(self, screen, sentence, font_color, font_name, font_size, center, left_top, right_bottom):
        self.screen = screen
        self.sentence = sentence
        self.font_color = font_color
        self.font = pygame.font.Font(os.path.join(self.FONT_PATH, font_name), font_size)
        self.center = center
        self.left_top = left_top
        self.right_bottom = right_bottom

    def display_text(self, new_sentence=''):
        self.sentence = new_sentence if new_sentence else self.sentence
        self.text = self.font.render(self.sentence, True, self.font_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.center
        self.screen.blit(self.text, self.textRect)

    def call_action_if_clicked(self, clicked_point, item_view_window, equipment, board, task_manager, stm):
        if not (self.left_top[0] <= clicked_point[0] <= self.right_bottom[0] and self.left_top[1] <= clicked_point[1] <= self.right_bottom[1]):
            return
        
        action_map = {
            'Take this item': self._take_item_action,
            'I don\'t need it': self._hide_item_action,
            'Exit': self._hide_item_action,
            'You can use {}'.format(item_view_window.current_item.interact_with): self._use_item_action,
            'You can repair the cube': self._repair_cube_action,
            'Enter the code': self._enter_code_action,
            'Enter the garage': self._enter_garage_action,
            'Enter the room': self._enter_room_action,
            'You can go to this place': self._go_to_place_action,
            'Use the cube and return home': self._use_cube_return_home_action,
            'You can tape the scheme': self._tape_scheme_action,
        }

        action = action_map.get(self.sentence)
        if action:
            action(item_view_window, equipment, board, task_manager, stm)
        else:
            print('No action with this textbox')

    def _take_item_action(self, item_view_window, equipment, board, task_manager, stm):
        item_view_window.current_item.is_active = 0
        equipment.add_item_to_equipment(item_view_window.current_item)
        item_to_remove = item_view_window.current_item
        item_view_window.hide_item()
        board.remove_item_from_board(item_to_remove)

    def _hide_item_action(self, item_view_window, equipment, board, task_manager, stm):
        if item_view_window.current_item.name == "Lock":
            task_manager.disable_flag("LOCK_ACTIVATED")
        item_view_window.current_item.is_active = 0
        item_view_window.hide_item()

    def _use_item_action(self, item_view_window, equipment, board, task_manager, stm):
        item_view_window.hide_item()
        equipment.remove_item()
        task_manager.enable_task_action("open_secret_box")

    def _repair_cube_action(self, item_view_window, equipment, board, task_manager, stm):
        item_view_window.hide_item()
        stm.write_sth("repair")
        equipment.add_item_to_equipment(board.generate_item("Repaired cube", "broken-cube-equip.png", "cube.png", "Repaired, I hope it will work"))
        task_manager.enable_task_action("repair_box")

    def _enter_code_action(self, item_view_window, equipment, board, task_manager, stm):
        if stm.write_sth("key") == "OK":
            item_view_window.hide_item()
            task_manager.enable_task_action("unlock_house_door")

    def _enter_garage_action(self, item_view_window, equipment, board, task_manager, stm):
        item_view_window.hide_item()
        task_manager.enable_task_action("open_garage_door")

    def _enter_room_action(self, item_view_window, equipment, board, task_manager, stm):
        if stm.write_sth("lcd") == "YES":
            item_view_window.hide_item()
            task_manager.enable_task_action("open_room_door")

    def _go_to_place_action(self, item_view_window, equipment, board, task_manager, stm):
        item_view_window.hide_item()
        task_manager.enable_task_action("follow_the_map")

    def _use_cube_return_home_action(self, item_view_window, equipment, board, task_manager, stm):
        item_view_window.hide_item()
        task_manager.enable_task_action("finish_game")

    def _tape_scheme_action(self, item_view_window, equipment, board, task_manager, stm):
        item_view_window.hide_item()
        equipment.add_item_to_equipment(board.generate_item("Repaired scheme", "note-small.png", "elec-scheme.png", "Ok I need to wire it up properly"))
        task_manager.enable_task_action("tape_scheme")

