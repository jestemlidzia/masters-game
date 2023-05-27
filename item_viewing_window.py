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
            {'sentence' : 'name', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 37), 'left_top' : (-1, -1), 'right_bottom': (-1, -1)},
            {'sentence' : 'dialog', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 457), 'left_top' : (-1, -1), 'right_bottom': (-1, -1)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (377, 555), 'left_top' : (188, 530), 'right_bottom': (583, 615)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (856, 557), 'left_top' : (655, 530), 'right_bottom': (1055, 615)},
            {'sentence' : 'option', 'color' : (198, 170, 33), 'font' : 'Eraser.ttf', 'size' : 32, 'center' : (640, 641), 'left_top' : (-1, -1), 'right_bottom': (-1, -1)}
        ]

        for info in textbox_info:
            info['sentence']
            new_textbox = textbox.TextBox(self.screen, info['sentence'], info['color'], info['font'], info['size'], info['center'], info['left_top'], info['right_bottom'])
            self.textbox_list.append(new_textbox)

    def show_item(self, current_item, equipment = None):
        print("ItemViewingWindow open")
        self.current_item = current_item
        self.is_visible = True
        self.last_screen = self.screen.copy()
        self.screen.blit(self.window_bg, (0,0))
        
        textbox_values = [self.current_item.name, self.current_item.dialog_text]
        if self.current_item.is_liftable:
            textbox_values += ['Take this item', 'I don\'t need it']
            if 'IS_XXX_ITEM_CAN_BE_USE' == 'TODO':
                textbox_values.append('You can use XXX')
            else:
                textbox_values.append('Nothing to do with it')

        for idx, tb in enumerate(self.textbox_list):
            tb.display_text(textbox_values[idx])

        showing_item = pygame.image.load(os.path.join("art", self.current_item.full_img))
        self.screen.blit(showing_item, (300,200))

    def hide_item(self):
        print("ItemViewingWindow hide")
        self.current_item = None
        self.is_visible = False
        self.screen.blit(self.last_screen, (0,0))