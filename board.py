import json
import pygame, os
import item

class Board(object):
    def __init__(self, screen, level_number):

        f = open('levels.json')
        data = json.load(f)
        f.close()

        self.screen = screen
        level_data = data['Levels'][level_number]

        print(level_data['Name'])
        self.level_name = level_data['Name']
        self.level_bg = pygame.image.load(os.path.join("art", level_data['BackgroungImg']))
        self.screen.blit(self.level_bg, (0,0))

        self.level_items = []
        for game_item in level_data['Items']:
            name = game_item['Name']
            img = game_item['Img']
            pos = (game_item['X-Position'], game_item['Y-Position'])
            is_movable = bool(game_item['IsMovable'])
            is_clickable = bool(game_item['IsClickable'])
            is_liftable = bool(game_item['IsLiftable'])
            is_active = bool(game_item['IsActive'])
            full_img = game_item['FullImg'] if is_clickable else None
            dialog_text = game_item['DialogText']
            new_item = item.Item(self.screen, name, is_movable, is_clickable, is_liftable, is_active, img, full_img, dialog_text, pos)
            self.level_items.append(new_item)

    def update_board(self):

        for item in self.level_items:
            item.update_item()