import pygame
import os

class Item:
    ART_PATH = "art"
    
    def __init__(self, screen, name, is_movable, is_clickable, is_liftable, is_active, 
                 change_slide, interact_with, img, full_img, equip_img, dialog_text, 
                 position=(0, 0)):
        self.screen = screen
        self.name = name
        self.is_movable = is_movable
        self.is_clickable = is_clickable
        self.is_liftable = is_liftable
        self.is_active = is_active
        self.change_slide = change_slide
        self.interact_with = interact_with
        self.dialog_text = dialog_text
        self.position = position
        
        self.set_image(img)
        self.full_img = full_img
        self.equip_img = equip_img

    def set_image(self, img):
        self.img = img
        self.game_item = pygame.image.load(os.path.join(self.ART_PATH, self.img))
        self.screen.blit(self.game_item, self.position)

    def update_item(self):
        self.screen.blit(self.game_item, self.position)
    
    def change_position(self, new_position):
        self.position = new_position

    def get_image_area(self):
        return self.game_item.get_rect(topleft=self.position)
    
    def get_image_size(self):
        return self.game_item.get_size()
    
    def change_item_image(self, new_img):
        print("New image:", new_img)
        self.set_image(new_img)
    
    def change_item_full_image(self, new_full_img):
        print("New full image:", new_full_img)
        self.full_img = new_full_img