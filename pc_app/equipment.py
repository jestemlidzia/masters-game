import pygame
import os
import board

class Equipment(object):
    def __init__(self, screen, level_number):

        self.screen = screen
        self.board = board.Board(self.screen, 0)

        self.backpack_view = pygame.image.load(os.path.join("art", 'equip.png'))
        self.active_area_view = pygame.image.load(os.path.join("art", 'active-box.png'))
        self.inactive_area_view = pygame.image.load(os.path.join("art", 'inactive-box.png'))

        self.screen.blit(self.backpack_view, (384,720))

        self.item_list = []
        self.cube_parts = ["Electronics element", "Battery", "Broken cube", "Resistor"]
        self.scheme_parts = ["Chinese food", "Wooden box", "The Ocean"]
        self.d = {}

        self.x_areas_range = [(384,447), (448, 511), (512, 575), (576, 639), (640, 703), (704, 767), (768, 831), (832, 895)]
        self.y_area_range = (650, 710)
        self.equip_size = 8

        self.is_open = False
        self.active_area_range = False
        self.selected_item = False
        self.is_selected = False

    def add_item_to_equipment(self, item):
        if len(self.item_list) < self.equip_size:
            self.item_list.append(item)
            print('The item {} has been put into the backpack'.format(item.name))
        else:
            print('Your backpack is full! Press "r" on the backpack item you want to discard to free up some space!')

    def print_backpack(self):
        if len(self.item_list) != 0:
            print('Items in your backpack:')
            for lifted_item in self.item_list:
                print(lifted_item.name)
        else:
            print('Your backpack is empty')

    def check_item_in_backpack(self, item_name):
        for i in range(len(self.item_list)):
            if item_name == self.item_list[i].name:
                print('{} is in the backpack'.format(item_name))
                return True
        else:
            print('There is no {} in the backpack'.format(item_name))
            return False
    
    def check_parts(self, number):
        count_elements = 0
        parts = self.cube_parts if number == 1 else self.scheme_parts
        for i in self.item_list:
            if i.name in parts:
                count_elements += 1
            if count_elements == len(parts):
                return True
        return False
    
    def repaired(self, number):
        new_list = []
        parts = self.cube_parts if number == 1 else self.scheme_parts
        for i in self.item_list:
            if i.name not in parts:
                new_list.append(i)
        self.item_list = new_list
     
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
        for i in range(len(self.x_areas_range)):
            if self.x_areas_range[i][0] <= pygame.mouse.get_pos()[0] <= self.x_areas_range[i][1] and self.y_area_range[0] <= pygame.mouse.get_pos()[1] <= self.y_area_range[1]:
                self.is_selected = False
                if self.active_area_range != False:
                    self.screen.blit(self.inactive_area_view, (self.active_area_range[0], self.y_area_range[0]))
                self.screen.blit(self.active_area_view, (self.x_areas_range[i][0], self.y_area_range[0]))
                self.active_area_range = (self.x_areas_range[i][0], self.x_areas_range[i][1])
                return self.active_area_range
        return False

    def update_equip(self):
        area_number = 0
        for item in self.item_list:
            if area_number < len(self.x_areas_range):
                showing_taken_item = pygame.image.load(os.path.join("art", item.equip_img))
                self.screen.blit(showing_taken_item, (self.x_areas_range[area_number][0]+20,self.y_area_range[0]+20))
                if self.active_area_range != False:
                    if self.active_area_range[0] > self.x_areas_range[area_number][0] or self.is_selected:          # > to odkliknięcie zaznaczonego elementu
                        self.selected_item = False
                    if self.active_area_range[0] == self.x_areas_range[area_number][0]:
                        self.selected_item = item
                area_number = area_number + 1

    def get_selected_item_name(self):
        if self.selected_item != False:
            print('The {} was selected'.format(self.selected_item.name))
            return self.selected_item.name
        return False

    def get_selected_item(self):
        if self.selected_item != False:
            print('The {} was selected'.format(self.selected_item.name))
            return self.selected_item
        return False
        
    def remove_item(self):
        if self.selected_item != False and len(self.item_list) != 0:
            self.item_list.remove(self.selected_item)
            self.screen.blit(self.backpack_view, (384,650))
            self.is_selected = True
