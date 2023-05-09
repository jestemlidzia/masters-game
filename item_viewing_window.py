import pygame, os, json
import item, textbox

class ItemViewingWindow(object):
    def __init__(self, screen, is_visible = False, current_item=None):

        f = open('levels.json')
        data = json.load(f)
        f.close()

        self.screen = screen
        self.last_screen = self.screen.copy()
        self.is_visible = is_visible
        self.current_item = current_item

        self.window_bg = pygame.image.load(os.path.join("art", data['ItemViewingWindow']['BackgroungImg']))

        self.textbox_list = []
        self.generate_textboxes()

    def generate_textboxes(self):
        textbox_info = [
            {'sentence' : 'name', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 37)},
            {'sentence' : 'dialog', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 457)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (377, 555)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (856, 557)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 641)}
        ]

        for info in textbox_info:
            info['sentence']
            new_textbox = textbox.TextBox(self.screen, info['sentence'], info['color'], info['font'], info['size'], info['center'])
            self.textbox_list.append(new_textbox)

    def show_item(self, current_item):
        print("ItemViewingWindow open")
        self.current_item = current_item
        self.is_visible = True
        self.last_screen = self.screen.copy()
        self.screen.blit(self.window_bg, (0,0))
        
        self.textbox_list[0].display_text(self.current_item.name)
        self.textbox_list[1].display_text(self.current_item.dialog_text)
        self.textbox_list[2].display_text('Take this item')
        self.textbox_list[3].display_text('I don\'t need it')
        self.textbox_list[4].display_text('Nothing to do with it')

        showing_item = pygame.image.load(os.path.join("art", self.current_item.full_img))
        self.screen.blit(showing_item, (300,200))

    def hide_item(self):
        print("ItemViewingWindow hide")
        self.current_item = None
        self.is_visible = False
        self.screen.blit(self.last_screen, (0,0))