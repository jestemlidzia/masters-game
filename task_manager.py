import pygame
import os

class TaskManager(object):
    def __init__(self, screen):
        self.screen = screen
        self.action_list = self.generate_task_list()
        self.screen_lock = False

    def generate_task_list(self):
        action_list = {
            "open_secret_box" : {
                "call_status" : False,
                "execution_status" : False
            },
            "another_task" : {
                "call_status" : False,
                "execution_status" : False   
            }
        }

        return action_list
    
    def enable_task_action(self, action_name):
        if action_name in self.action_list:
            self.action_list[action_name]["call_status"] = True

    def monitor_tasks(self):
        for action in self.action_list:
            if self.action_list[action]["call_status"] == True and self.action_list[action]["execution_status"] == False:
                return self.execute_action(action)

    def execute_action(self, action_name):
        if action_name == "open_secret_box":
            print("--- Opening a secret box ---")
            self.action_list[action_name]["execution_status"] = True
            self.show_animation(["slide1.png", "slide2.png", "slide1.png", "slide3.png"])
            return True
        elif action_name == "another_task":
            return False
        else:
            return False
    
    def show_animation(self, files):
        self.screen_lock = True
        last_screen = self.screen.copy()

        for file in files:
            image_size = (1664, 936)
            animation_bg = pygame.image.load(os.path.join("art", file))
            
            for x in range(0, 50, 2):
                image_size = (image_size[0] * 0.999, image_size[1] * 0.999)
                image_shift = ((1280 - image_size[0])//2, (720 - image_size[1])//2)
                animation_bg = pygame.transform.smoothscale(animation_bg, (image_size))
                self.screen.blit(animation_bg, (image_shift))
                pygame.display.update()
                pygame.time.wait(130)

                # image = pygame.image.load('your_image.png').convert()
                # image_rect = image.get_rect()
                # image_rect.center = (100,100)

        self.screen.blit(last_screen, (0,0))
        self.screen_lock = False