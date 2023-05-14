import item
import pygame, os
import json
import board

class Equipment(object):
    def __init__(self, screen, level_number):

        # f = open('levels.json')
        # data = json.load(f)
        # f.close()

        self.screen = screen
        # level_data = data['Levels'][level_number]
        # self.level_name = level_data['Name']

        self.board = board.Board(self.screen, 0)

        self.backpack_view = pygame.image.load(os.path.join("art", 'equip.png'))
        self.active_area_view = pygame.image.load(os.path.join("art", 'active-box.png'))
        self.inactive_area_view = pygame.image.load(os.path.join("art", 'inactive-box.png'))
        # self.equip_item = pygame.image.load(os.path.join("art", level_data['EquipImage']))

        self.screen.blit(self.backpack_view, (384,720))
        
        # (384, 650) is visible

        self.img = []
        self.item_list = []
        self.x_areas_range = [(384,447), (448, 511), (512, 575), (576, 639), (640, 703), (704, 767), (768, 831), (832, 895)]
        self.y_area_range = (650, 710)
        self.is_open = False
        self.active_area_range = False

    def add_item_to_equipment(self, item):
        self.item_list.append(item)
        # self.img.append(item.name + '-equip.png')
        print('The item {} has been put into the backpack'.format(item.name))

    def print_backpack(self):
        if len(self.item_list)!=0:
            print('Items in your backpack:')
            for lifted_item in self.item_list:
                print(lifted_item.name)
        else:
            print('Your backpack is empty')

    def check_item_in_backpack(self, item_name):
        # if item in self.item_list:
        for i in range(len(self.item_list)):
            if item_name == self.item_list[i].name:
                print('{} is in the backpack'.format(item_name))
                return True
        else:
            print('There is no {} in the backpack'.format(item_name))
            return False
        
    def show_backpack(self):
        self.last_screen = self.screen.copy()
        print("Backpack open")
        self.screen.blit(self.backpack_view, (384,650))
        self.is_open = True

    def hide_backpack(self):
        print("Backpack hide")
        self.screen.blit(self.last_screen, (0,0))
        self.is_open = False

    def selected_area(self):
        self.last_screenn = self.screen.copy()
        for i in range(len(self.x_areas_range)):
            if self.x_areas_range[i][0] <= pygame.mouse.get_pos()[0] <= self.x_areas_range[i][1] and self.y_area_range[0] <= pygame.mouse.get_pos()[1] <= self.y_area_range[1]:
                if self.active_area_range != False:
                    self.hide_selected_area(self.active_area_range)
                self.screen.blit(self.active_area_view, (self.x_areas_range[i][0], self.y_area_range[0]))
                self.active_area_range = (self.x_areas_range[i][0], self.x_areas_range[i][1])
                return self.active_area_range
        return False
    
    def hide_selected_area(self, cords):
        self.screen.blit(self.inactive_area_view, (cords[0], self.y_area_range[0]))

    def update_equip(self):
        # for item in self.item_list:
        #     self.img.append(item.name + '-equip.png')
        print('aoaoao', self.board.level_items)
        print('aoaod', self.item_list)
        
        # for item in self.board.level_items:
        #     print(item.name)
        #     if item.name == self.item_list[item].name:
        #         print(item.EquipImage, 'sss')
        #         self.equip_item = pygame.image.load(os.path.join("art", item.EquipImage))
        #         self.screen.blit(self.equip_item, (self.x_areas_range[item][0], self.y_area_range[0]+20))

    def get_image_area(self):
        return self.game_item.get_rect(topleft = self.position)

    def select_item(self):
        print('TODO')

    def remove_item(self):
        print('TODO')
    
