import pygame
import os

class TaskManager(object):
    def __init__(self, screen, board, equipment, stm):
        self.screen = screen
        self.board = board
        self.action_list = self.generate_task_list()
        self.game_flags = self.generate_game_flags()
        self.screen_lock = False
        self.equipment = equipment
        self.stm = stm

    def generate_game_flags(self):
        game_flags = {
            "LOCK_ACTIVATED" : False,
            "CUBE_IS_REPAIRED" : False,
            "SCHEME_IS_TAPED" : False,
            "GARAGE_DOOR_UNLOCKED" : False,
            "ROOM_DOOR_UNLOCKED" : False,
            "CHAT_WITH_SAM_ENDED" : False,
            "SOUND_ENERGY_COLLECTED" : False,
            "INDICATOR_LEVEL" : 0,
            "LISTENING" : True
        }
        return game_flags

    def generate_task_list(self):
        action_list = {
            "open_secret_box" : {
                "call_status" : False,
                "execution_status" : False
            },
            "repair_box" : {
                "call_status" : False,
                "execution_status" : False
            },
            "another_task" : {
                "call_status" : False,
                "execution_status" : False
            },
            "activate_lock" : {
                "call_status" : False,
                "execution_status" : False
            },
            "unlock_house_door" : {
                "call_status" : False,
                "execution_status" : False
            },
            "tape_scheme" : {
                "call_status" : False,
                "execution_status" : False
            },
            "open_garage_door" : {
                "call_status" : False,
                "execution_status" : False
            },
            "open_room_door" : {
                "call_status" : False,
                "execution_status" : False
            },
            "follow_the_map" :  {
                "call_status" : False,
                "execution_status" : False
            },
            "increase_indicator_level" :  {
                "call_status" : False,
                "execution_status" : False
            },
            "unlock_energy_box" :  {
                "call_status" : False,
                "execution_status" : False
            },
            "finish_game" :  {
                "call_status" : False,
                "execution_status" : False
            }
        }

        return action_list

    def enable_flag(self, flag):
        if flag in self.game_flags:
            self.game_flags[flag] = True

    def disable_flag(self, flag):
        if flag in self.game_flags:
            self.game_flags[flag] = False

    def enable_task_action(self, action_name):
        if action_name in self.action_list:
            self.action_list[action_name]["call_status"] = True

    def disable_task_action(self, action_name):
        if action_name in self.action_list:
            self.action_list[action_name]["call_status"] = False

    def monitor_tasks(self):
        if self.game_flags["LISTENING"]:
            if self.board.level_number == 5:
                if "ON" == self.stm.write_sth("diode"):
                    self.enable_flag("GARAGE_DOOR_UNLOCKED")
                    item = self.board.get_item_by_its_name("Garage lock")
                    item.change_item_image("door-unlocked-small.png")
                    item.change_item_full_image("door-unlocked.png")
                elif "OFF" == self.stm.write_sth("diode"):
                    self.disable_flag("GARAGE_DOOR_UNLOCKED")
                    item = self.board.get_item_by_its_name("Garage lock")
                    item.change_item_image("door-locked-small.png")
                    item.change_item_full_image("door-locked.png")
                else:
                    print("Unknow status of DIODE")
            if self.board.level_number == 8 and not self.game_flags["SOUND_ENERGY_COLLECTED"]:
                if "OKK" == self.stm.write_sth("volume"):
                    self.enable_task_action("increase_indicator_level")
                else:
                    print("Too quiet!!!")


        for action in self.action_list:
            if self.action_list[action]["call_status"] == True and self.action_list[action]["execution_status"] == False:
                return self.execute_action(action)

    def execute_action(self, action_name):
        if action_name == "open_secret_box":
            print("--- Opening a secret box ---")
            self.action_list[action_name]["execution_status"] = True
            self.show_animation(["cube-slide.png", "level2-slide.png"])
            self.board.load_new_level_elements(1)
            return True
        elif action_name == "repair_box":
            print("--- Secret box has been repaired ---")
            self.action_list[action_name]["execution_status"] = True
            self.equipment.repaired(1)
            self.enable_flag("CUBE_IS_REPAIRED")
            self.show_slide("cube_is_repaired.png")
            return False
        elif action_name == "unlock_house_door":
            if self.game_flags["LOCK_ACTIVATED"] and self.game_flags["CUBE_IS_REPAIRED"]:
                print("--- The house door is opened ---")
                self.action_list[action_name]["execution_status"] = True
                self.show_animation(["level3-slide.png"])
                self.board.load_new_level_elements(4)
                return True
            else:
                self.action_list[action_name]["call_status"] == False
                return False
        elif action_name == "tape_scheme":
            print("--- Scheme has been taped ---")
            self.action_list[action_name]["execution_status"] = True
            self.equipment.repaired(2)
            self.enable_flag("SCHEME_IS_TAPED")
            self.show_slide("schematic_is_repaired.png")
        elif action_name == "open_garage_door":
            if self.game_flags["GARAGE_DOOR_UNLOCKED"]:
                self.action_list[action_name]["execution_status"] = True
                self.show_animation(["level4-slide.png"])
                self.board.load_new_level_elements(6)
                return True
        elif action_name == "open_room_door":
            if self.game_flags["ROOM_DOOR_UNLOCKED"]:
                self.action_list[action_name]["execution_status"] = True
                self.show_animation(["level5-slide.png"])
                self.board.load_new_level_elements(8)
                return True
        elif action_name == "follow_the_map":
            print("--- Tunnel level is active ---")
            self.action_list[action_name]["execution_status"] = True
            self.board.load_new_level_elements(7)
            return True
        elif action_name == "increase_indicator_level":
            item = self.board.get_item_by_its_name("Indicator")
            self.game_flags["INDICATOR_LEVEL"] += 1
            item.change_item_image("scale-" + str(self.game_flags["INDICATOR_LEVEL"]) + ".png")
            if self.game_flags["INDICATOR_LEVEL"] == 3:
                self.enable_flag("SOUND_ENERGY_COLLECTED")
                self.action_list[action_name]["execution_status"] = True
                self.enable_task_action("unlock_energy_box")
            else:
                self.action_list[action_name]["call_status"] = False
            return False
        elif action_name == "unlock_energy_box":
            item = self.board.get_item_by_its_name("Energy box")
            item.change_item_image("energy-box-opened-small.png")
            item.change_item_full_image("energy-box-opened.png")
            item.dialog_text = ("Now I can use it")
            self.action_list[action_name]["execution_status"] = True
            return False
        elif action_name == "finish_game":
            print("--- Game is ended ---")
            self.action_list[action_name]["execution_status"] = True
            self.show_slide("ending_slide.png")
            self.show_animation(["the-end.png"])
            return False
        elif action_name == "another_task":
            return False
        else:
            return False

    def show_slide(self, file):
        self.screen_lock = True
        last_screen = self.screen.copy()

        animation_bg = pygame.image.load(os.path.join("art", file))
        self.screen.blit(animation_bg, (0,0))
        pygame.display.update()
        pygame.time.wait(3000)
        
        self.screen.blit(last_screen, (0,0))
        self.screen_lock = False

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

        self.screen.blit(last_screen, (0,0))
        self.screen_lock = False

    def show_dialog(self, files):
        self.screen_lock = True
        last_screen = self.screen.copy()

        for file in files:
            dialog_bg = pygame.image.load(os.path.join("art", file))
            dialog_effect = pygame.image.load(os.path.join("art", "dialog_effect.png"))
            self.screen.blit(dialog_bg, (0,0))

            for x in range(0, 10):
                pygame.display.update()
                pygame.time.wait(1000)
                self.screen.blit(dialog_effect, (0,0))

        pygame.time.wait(100)
        self.screen.blit(last_screen, (0,0))
        self.screen_lock = False