import item
import pygame, os

class Equipment(object):
    def __init__(self, screen):
        self.screen = screen
        self.backpack_view = pygame.image.load(os.path.join("art", 'equip.png'))
        self.screen.blit(self.backpack_view, (384,720))
        
        # (384, 650) is visible

        self.item_list = []
        self.x_areas_range = [(384,577), (578, 771), (772, 965), (966, 1159), (1160, 1353), (1354, 1547), (1548, 1741), (1742, 1935)]
        self.y_area_range = (650, 710)
        self.is_open = False

    def add_item_to_equipment(self, item):
        self.item_list.append(item)
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

    def find_active_area(self):
        for i in range(len(self.x_areas_range)):
            if self.x_areas_range[i][0] <= pygame.mouse.get_pos()[0] <= self.x_areas_range[i][1] and self.y_area_range[0] <= pygame.mouse.get_pos()[1] <= self.y_area_range[1]:
                # self.screen.blit(self.backpack_view, (384,650))
                print(len(self.x_areas_range),'ola')

    def update_equip(self):
        if self.is_movable: # jesli przedmiot jest w plecaku to wyswitl go w equip
            self.screen.blit(self.game_item, self.position)

    def get_image_area(self):
        return self.game_item.get_rect(topleft = self.position)

    def select_item(self):
        print('TODO')

    def remove_item(self):
        print('TODO')
    
