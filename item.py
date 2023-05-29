import pygame, os

class Item(object):
    def __init__(self, screen, name, is_movable, is_clickable, is_liftable, is_active, img, full_img, equip_img, dialog_text, position = (0,0)):
        self.screen = screen
        self.name = name
        self.is_movable = is_movable
        self.is_clickable = is_clickable
        self.is_liftable = is_liftable
        self.is_active = is_active
        self.img = img
        self.full_img = full_img
        self.equip_img = equip_img
        self.position = position
        self.dialog_text = dialog_text

        self.game_item = pygame.image.load(os.path.join("art", img))
        self.screen.blit(self.game_item, self.position)

    def update_item(self):
        self.screen.blit(self.game_item, self.position)
    
    def change_position(self, new_position):
        self.position = new_position

    def get_image_area(self):
        return self.game_item.get_rect(topleft = self.position)
    
    def get_image_size(self):
        x = self.game_item.get_width()
        y = self.game_item.get_height()

        return (x,y)