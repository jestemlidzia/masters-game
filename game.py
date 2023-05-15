import pygame, sys, os
import board
import textbox
import equipment
import item_viewing_window

class Game(object):
    def __init__(self):
        pygame.font.init()

        self.height = 720
        self.width = 1280

        pygame.display.set_caption('Ola&Lidka')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width,self.height))

        self.board = board.Board(self.screen, 0)
        self.equipment = equipment.Equipment(self.screen, 0)
        self.item_view_window = item_viewing_window.ItemViewingWindow(self.screen)
    

    def update(self):
        # Handle events
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.equipment.is_open:
                    self.equipment.selected_area()
                if not self.item_view_window.is_visible:
                    for board_item in self.board.level_items:
                        is_collidate = board_item.get_image_area().collidepoint(event.pos)
                        if is_collidate and board_item.is_clickable:
                            print('clicked on image', board_item.name)
                            self.item_view_window.show_item(board_item)
                            print(self.item_view_window.is_visible)

                            board_item.is_active = 1
                            print('Test liftable', board_item.name, " : ", board_item.is_liftable)
                            print('Test active', board_item.name, " : ", board_item.is_active)
                else:
                    for textbox in self.item_view_window.textbox_list:
                        textbox.call_action_if_clicked(pygame.mouse.get_pos(), self.item_view_window, self.equipment)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if self.equipment.is_open == False:
                        self.equipment.print_backpack()
                        self.equipment.show_backpack()
                        # self.equipment.update_equip()
                    else:
                        self.equipment.hide_backpack()
                    # self.equipment.check_item_in_backpack('Book')
                    

        self.board.update_board()
        pygame.display.update()
        self.clock.tick(60)

    def change_level(self, level_number):
        print('Next level')
        #update bg, new_items = new board