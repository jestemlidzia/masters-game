import pygame
import sys
import board
import equipment
import item_viewing_window
import task_manager
import stm

class Game(object):
    def __init__(self):
        pygame.font.init()
        self._init_display()
        self._init_game_components()
        self._show_initial_dialog_and_animation()

    def _init_display(self):
        self.height = 720
        self.width = 1280
        pygame.display.set_caption('ON THE OTHER SIDE')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

    def _init_game_components(self):
        self.board = board.Board(self.screen, 0)
        self.equipment = equipment.Equipment(self.screen, 0)
        self.item_view_window = item_viewing_window.ItemViewingWindow(self.screen)
        self.stm = stm.STM()
        self.stm.find_port()
        self.stm.board_connection()
        self.task_manager = task_manager.TaskManager(self.screen, self.board, self.equipment, self.stm)
        self.level_number = 1

    def _show_initial_dialog_and_animation(self):
        self.task_manager.show_dialog(["opening_dialog_1.png", "opening_dialog_2.png"])
        self.task_manager.show_animation(["level1-slide.png"])

    def update(self):
        self._handle_events()
        self._update_game_state()
        pygame.display.update()
        self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event)
            elif event.type == pygame.KEYDOWN:
                self._handle_key_press(event)

    def _handle_mouse_click(self, event):
        if self.equipment.is_open:
            self.equipment.selected_area()
            return
        if self.item_view_window.is_visible:
            for textbox in self.item_view_window.textbox_list:
                textbox.call_action_if_clicked(event.pos, self.item_view_window, self.equipment, self.board, self.task_manager, self.stm)
            return
        for board_item in self.board.level_items:
            self._process_board_item_click(event, board_item)

    def _process_board_item_click(self, event, board_item):
        is_collidate = board_item.get_image_area().collidepoint(event.pos)
        if is_collidate:
            if board_item.is_clickable:
                self._handle_clickable_item(board_item)
            else:
                self._handle_non_clickable_item(board_item)

    def _handle_clickable_item(self, board_item):
        self.task_manager.disable_flag("LISTENING")
        if self.equipment.is_open:
            self.equipment.hide_backpack()
        selected_item = self.equipment.get_selected_item_name()
        if board_item.name == "Sam":
            self.task_manager.show_dialog(["dialog_3.png"])
            self.task_manager.enable_flag("CHAT_WITH_SAM_ENDED")
        else:
            self.item_view_window.show_item(board_item, selected_item, self.equipment, self.task_manager)
            board_item.is_active = 1

    def _handle_non_clickable_item(self, board_item):
        if board_item.change_slide != "none":
            print(board_item.change_slide, "!!!!")
            self.board.load_new_level_elements(board_item.change_slide)
            if self.board.level_number == 4:
                self.stm.write_sth('off')

    def _handle_key_press(self, event):
        if event.key == pygame.K_b:
            self._toggle_equipment()
        elif event.key == pygame.K_r:
            self.equipment.remove_item()
        elif event.key == pygame.K_o:
            selected_item = self.equipment.get_selected_item()
            self.equipment.hide_backpack()
            self.item_view_window.show_item(selected_item, None, self.equipment, self.task_manager)

    def _toggle_equipment(self):
        if self.equipment.is_open:
           self.equipment.hide_backpack()
        else:
            self.equipment.print_backpack()
            self.equipment.show_backpack()

    def _update_game_state(self):
        if self.equipment.is_open:            
            self.equipment.update_equip()
        elif not self.item_view_window.is_visible and not self.task_manager.screen_lock:
            self.task_manager.enable_flag("LISTENING")
            self.board.update_board()
        if self.task_manager.monitor_tasks():
            self.change_level()

    def change_level(self):
        print('Next level')