import pygame, sys, os
import board
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
                else:
                    self.item_view_window.hide_item()

        self.board.update_board()
        pygame.display.update()
        self.clock.tick(60)

    def change_level(self, level_number):
        print('Next level')
        #update bg, new_items = new board