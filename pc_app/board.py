import os
import json
import pygame
import item

class Board(object):
    def __init__(self, screen, level_number):
        self.data = self._load_level_data()
        self.screen = screen
        self.level_number = level_number
        self.level_items = []
        self.taken_elements = []
        self.load_new_level_elements(level_number)

    @staticmethod
    def _load_level_data():
        with open('levels.json', 'r') as f:
            return json.load(f)

    def _generate_level_items_list(self, level_data):
        for game_item in level_data['Items']:
            name = game_item['Name']
            if name in self.taken_elements:
                continue
            new_item = self._create_item_from_data(game_item)
            self.level_items.append(new_item)

    def _create_item_from_data(self, game_item):
        return item.Item(
            self.screen,
            game_item['Name'],
            game_item.get('IsMovable', False),
            game_item.get('IsClickable', False),
            game_item.get('IsLiftable', False),
            game_item.get('IsActive', False),
            game_item.get('ChangeSlide', None),
            game_item['InteractWith'],
            game_item['Img'],
            game_item.get('FullImg', None),
            game_item.get('EquipImage', None),
            game_item['DialogText'],
            (game_item['X-Position'], game_item['Y-Position'])
        )

    def generate_item(self, item_name, item_equip, item_full_img, item_dialog):
        return item.Item(
            self.screen, item_name, None, True, False, None, None, "none",
            "cube-small.png", item_full_img, item_equip, item_dialog, (0, 0)
        )

    def get_item_by_its_name(self, item_name):
        for current_item in self.level_items:
            if current_item.name == item_name:
                return current_item
        return None

    def load_new_level_elements(self, level_number):
        self.level_number = level_number
        self.level_items.clear()
        level_data = self.data['Levels'][level_number]
        self.level_name = level_data['Name']
        self.level_bg = pygame.image.load(os.path.join("art", level_data['BackgroungImg']))
        self.screen.blit(self.level_bg, (0, 0))
        self.initial_screen = self.screen.copy()
        self._generate_level_items_list(level_data)

    def update_board(self):
        self.screen.blit(self.level_bg, (0, 0))
        for current_item in self.level_items:
            current_item.update_item()

    def remove_item_from_board(self, target_item):
        self.level_items.remove(target_item)
        self.screen.blit(self.initial_screen, (0, 0))
        self.taken_elements.append(target_item.name)