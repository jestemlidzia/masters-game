import pygame, os, json
import item, textbox
import equipment

class ItemViewingWindow(object):
    def __init__(self, screen, is_visible = False, current_item=None, interact_with = None):

        f = open('levels.json')
        data = json.load(f)
        f.close()

        self.screen = screen
        self.last_screen = self.screen.copy()
        self.is_visible = is_visible
        self.current_item = current_item
        self.interact_with = interact_with

        self.window_bg = pygame.image.load(os.path.join("art", data['ItemViewingWindow']['BackgroungImg']))

        self.textbox_list = []
        self.generate_textboxes()

        self.equipment = equipment.Equipment(self.screen, 0)
        print('test',self.equipment.get_selected_item())

    def generate_textboxes(self):
        textbox_info = [
            {'sentence' : 'name', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 37), 'left_top' : (-1, -1), 'right_bottom': (-1, -1)},
            {'sentence' : 'dialog', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 457), 'left_top' : (-1, -1), 'right_bottom': (-1, -1)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (377, 555), 'left_top' : (188, 530), 'right_bottom': (583, 615)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (856, 557), 'left_top' : (655, 530), 'right_bottom': (1055, 615)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 641), 'left_top' : (285, 617), 'right_bottom': (970, 667)}
        ]

        for info in textbox_info:
            info['sentence']
            new_textbox = textbox.TextBox(self.screen, info['sentence'], info['color'], info['font'], info['size'], info['center'], info['left_top'], info['right_bottom'])
            self.textbox_list.append(new_textbox)

    def show_item(self, current_item, selected_equip_item, equipment, task_manager):
        print("ItemViewingWindow open")
        print(self.current_item)
        self.current_item = current_item
        self.selected_equip_item = selected_equip_item
        self.is_visible = True
        self.last_screen = self.screen.copy()
        self.screen.blit(self.window_bg, (0,0))
        textbox_values = [self.current_item.name, self.current_item.dialog_text]
        if self.current_item.is_clickable:
            if self.current_item.is_liftable:
                textbox_values += ['Take this item', 'I don\'t need it']
            else:
                textbox_values += ['---', 'Exit']

            if self.current_item.name == "Energy box" and task_manager.game_flags["SOUND_ENERGY_COLLECTED"] and self.current_item.interact_with == self.selected_equip_item:
                textbox_values.append("Use the cube and return home")
            elif self.current_item.interact_with == self.selected_equip_item and self.current_item.name != "Energy box":           # sprawdzenie czy po wybraniu np chisel z plecaka, zmienia sie akcja na kostce
                textbox_values.append('You can use {}'.format(self.current_item.interact_with))
            elif equipment.check_parts(1) and self.current_item.name == "Toolbox":
                textbox_values.append('You can repair the cube')
            elif self.current_item.name == "Lock" and equipment.check_item_in_backpack("Repaired cube"):
                textbox_values.append('Enter the code')
                task_manager.enable_flag("LOCK_ACTIVATED")
            elif self.current_item.name == "Garage lock" and task_manager.game_flags["GARAGE_DOOR_UNLOCKED"]:
                textbox_values.append('Enter the garage')
            elif self.current_item.name == "Tunnel lock":
                textbox_values.append('Enter the room')
                task_manager.enable_flag("ROOM_DOOR_UNLOCKED")
            elif self.current_item.name == "Map" and task_manager.game_flags["CHAT_WITH_SAM_ENDED"]:
                textbox_values.append("You can go to this place")
            elif equipment.check_parts(2) and self.current_item.name == "Tape":
                textbox_values.append("You can tape the scheme")
            else:
                textbox_values.append('Nothing to do with it')
        for idx, tb in enumerate(self.textbox_list):
            print(tb)
            tb.display_text(textbox_values[idx])

        showing_item = pygame.image.load(os.path.join("art", self.current_item.full_img))

        x = 640 - (showing_item.get_width())/2
        y = 158 + 85 - (showing_item.get_height())/2
        self.screen.blit(showing_item, (x,y))

    def hide_item(self):
        print("ItemViewingWindow hide")
        self.current_item = None
        self.is_visible = False
        self.screen.blit(self.last_screen, (0,0))