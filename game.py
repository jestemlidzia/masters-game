import pygame, sys, os
import board
import textbox
import equipment
import item_viewing_window
import task_manager
import stm
import threadss

class Game(object):
    def __init__(self):
        pygame.font.init()

        self.height = 720
        self.width = 1280
        
        pygame.display.set_caption('ON THE OTHER SIDE')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width,self.height))

        self.board = board.Board(self.screen, 4)
        self.equipment = equipment.Equipment(self.screen, 0)
        self.item_view_window = item_viewing_window.ItemViewingWindow(self.screen)
        self.stm = stm.STM()
        self.threadss = threadss.Threadss()

        self.stm.find_port()
        self.stm.board_connection()
        # self.threadss.run_thread(self.stm.read_sth())

        self.task_manager = task_manager.TaskManager(self.screen, self.board, self.equipment, self.stm)
        # self.task_manager.show_dialog(["opening_dialog_1.png", "opening_dialog_2.png"])
        # self.task_manager.show_animation(["level1-slide.png"])

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
                            self.task_manager.disable_flag("LISTENING")
                            if self.equipment.is_open:
                                self.equipment.hide_backpack()
                            get_selected_item = self.equipment.get_selected_item_name()
                            if board_item.name == "Sam":
                                self.task_manager.show_dialog(["dialog_3.png"])
                                self.task_manager.enable_flag("CHAT_WITH_SAM_ENDED")
                            else:
                                self.item_view_window.show_item(board_item, get_selected_item, self.equipment, self.task_manager)
                                board_item.is_active = 1
                        if is_collidate and board_item.is_clickable == 0:
                            if board_item.change_slide != "none":
                                self.board.load_new_level_elements(board_item.change_slide)
                                if self.board.level_number == 4:
                                    self.stm.write_sth('off')
                else:
                    for textbox in self.item_view_window.textbox_list:
                        textbox.call_action_if_clicked(pygame.mouse.get_pos(), self.item_view_window, self.equipment, self.board, self.task_manager, self.stm)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if self.equipment.is_open == False:
                        self.equipment.print_backpack()
                        self.equipment.show_backpack()
                    else:
                        self.equipment.hide_backpack()
                        # self.equipment.get_selected_item()
                    # self.equipment.check_item_in_backpack('Book')
                if event.key == pygame.K_r:
                    if self.equipment.is_open:
                        self.equipment.remove_item()
                if event.key == pygame.K_o:
                    selected_item = self.equipment.get_selected_item()
                    print("OBIEKT: ", selected_item)
                    self.item_view_window.show_item(selected_item, None, self.equipment, self.task_manager)
                    #self.task_manager.show_dialog(["dialog_3.png"])

        if self.equipment.is_open:            
            self.equipment.update_equip()
            #self.equipment.get_selected_item()
            
        if not self.item_view_window.is_visible and not self.task_manager.screen_lock and not self.equipment.is_open:
            self.task_manager.enable_flag("LISTENING")
            self.board.update_board()      

        if self.task_manager.monitor_tasks():
            self.change_level()
 
        # if self.board.level_number == 8:
        #     self.stm.write_sth('volume')

        pygame.display.update()
        self.clock.tick(60)

    def change_level(self):
        print('Next level')
        #self.level_number += 1
        print("NOWY SCREEN")
        # self.screen = new_screen
        #update bg, new_items = new board
