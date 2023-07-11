import pygame, sys, os
import board
import textbox
import equipment
import item_viewing_window
import task_manager

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

        self.task_manager = task_manager.TaskManager(self.screen)

        self.level_number = 1

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
                            if self.equipment.is_open:
                                self.equipment.hide_backpack()
                            get_selected_item = self.equipment.get_selected_item()
                            self.item_view_window.show_item(board_item, get_selected_item)
                            board_item.is_active = 1
                else:
                    for textbox in self.item_view_window.textbox_list:
                        textbox.call_action_if_clicked(pygame.mouse.get_pos(), self.item_view_window, self.equipment, self.board)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if self.equipment.is_open == False:
                        self.equipment.print_backpack()
                        self.equipment.show_backpack()
                    else:
                        self.equipment.hide_backpack()
                        self.equipment.get_selected_item()
                    # self.equipment.check_item_in_backpack('Book')
                if event.key == pygame.K_r:
                    if self.equipment.is_open:
                        self.equipment.remove_item()
        if self.equipment.is_open:            
            self.equipment.update_equip()
            self.equipment.get_selected_item()
            
        if not self.item_view_window.is_visible and not self.task_manager.screen_lock:
            self.board.update_board()      

        if self.task_manager.monitor_tasks():
            self.change_level()

        pygame.display.update()
        self.clock.tick(60)

    def change_level(self):
        print('Next level')
        self.level_number += 1
        print("NOWY SCREEN")
        # self.screen = new_screen
        #update bg, new_items = new board