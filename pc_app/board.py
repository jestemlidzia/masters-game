import json
import pygame, os
import item

class Board(object):
    def __init__(self, screen, level_number):

        f = open('levels.json')
        self.data = json.load(f)
        f.close()

        self.level_number = level_number
        self.screen = screen
        self.level_items = []
        self.taken_elements = []

        self.load_new_level_elements(level_number)

    def generate_level_items_list(self, level_data):
        for game_item in level_data['Items']:
            name = game_item['Name']
            img = game_item['Img']
            pos = (game_item['X-Position'], game_item['Y-Position'])
            is_movable = bool(game_item['IsMovable'])
            is_clickable = bool(game_item['IsClickable'])
            is_liftable = bool(game_item['IsLiftable'])
            is_active = bool(game_item['IsActive'])
            change_slide = game_item['ChangeSlide'] if is_clickable == 0 else None
            interact_with = game_item['InteractWith']
            full_img = game_item['FullImg'] if is_clickable else None
            equip_img = game_item['EquipImage'] if is_liftable else None
            dialog_text = game_item['DialogText']
            if name in self.taken_elements:
                continue
            new_item = item.Item(self.screen, name, is_movable, is_clickable, is_liftable, is_active, change_slide, interact_with, img, full_img, equip_img, dialog_text, pos)
            self.level_items.append(new_item)

    def generate_item(self, item_name, item_equip, item_full_img, item_dialog):
        name = item_name
        img = "cube-small.png"
        pos = (0, 0)
        is_movable = None
        is_clickable = 1
        is_liftable = 0
        is_active = None
        change_slide = None
        interact_with = "none"
        full_img = item_full_img
        equip_img = item_equip
        dialog_text = item_dialog
        generated_item = item.Item(self.screen, name, is_movable, is_clickable, is_liftable, is_active, change_slide, interact_with, img, full_img, equip_img, dialog_text, pos)
        return generated_item


    def get_item_by_its_name(self, item_name):
        for item in self.level_items:
            if item.name == item_name:
                return item
            
        return None

    def load_new_level_elements(self, level_number):
        self.level_number = level_number
        self.level_items = []
        level_data = self.data['Levels'][level_number]
        self.level_name = level_data['Name']
        self.level_bg = pygame.image.load(os.path.join("art", level_data['BackgroungImg']))
        self.screen.blit(self.level_bg, (0,0))

        self.initial_screen = self.screen.copy()

        self.generate_level_items_list(level_data)

    def update_board(self):
        self.screen.blit(self.level_bg, (0,0))
        for item in self.level_items:
            item.update_item()

    def remove_item_from_board(self, item):
        self.level_items.remove(item)
        self.screen.blit(self.initial_screen, (0,0))
        self.taken_elements.append(item.name)