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
        self.equipment = equipment.Equipment()
        self.item_view_window = item_viewing_window.ItemViewingWindow(self.screen)
    

    def update(self):
        # Handle events
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                    for item in self.board.level_items:
                        if item.is_active:
                            if item.is_liftable:
                                if 188 <= pygame.mouse.get_pos()[0] <= 583 and 530 <= pygame.mouse.get_pos()[1] <= 615:
                                    item.is_active = 0
                                    self.equipment.add_item_to_equipment(item)
                                    self.item_view_window.hide_item()
                            else:
                                if 188 <= pygame.mouse.get_pos()[0] <= 583 and 530 <= pygame.mouse.get_pos()[1] <= 615:
                                    print("Item {} can'it be put into backpack".format(item.name))
                                    # self.item_view_window.hide_item()
                            if 655 <= pygame.mouse.get_pos()[0] <= 1055 and 530 <= pygame.mouse.get_pos()[1] <= 615:
                                item.is_active = 0
                                self.item_view_window.hide_item()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    self.equipment.print_backpack()
                    # self.equipment.check_item_in_backpack('Book')
                    

        self.board.update_board()
        pygame.display.update()
        self.clock.tick(60)

    def change_level(self, level_number):
        print('Next level')
        #update bg, new_items = new board