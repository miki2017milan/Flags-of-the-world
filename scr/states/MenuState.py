import pygame as py
py.init()

from scr.states.State import State
from scr.states.CollectionState import CollectionState

from scr.utils import Utils, Config
from scr.Assets import Assets

from gui.Button import Button

class MenuState(State):
    def __init__(self, main):
        super().__init__(main)

        self.collection_state = CollectionState(main)

        self.current_state = self.collection_state

        self.NORMAL_BUTTON_COLOR = (255, 255, 255)
        self.HIGHLIGHT_BUTTON_COLOR = (130, 130, 130)
        self.collection_buttons = []
        for i, k in enumerate(Assets.COLLECTIONS.keys()):
            button = Button(25, 300 + 100 * i, 250, 80, k, 20, 10, 10, 20, 5, (26, 120, 210), self.NORMAL_BUTTON_COLOR, (255, 255, 255), font_art="Calibri")
            button.center_text_x()
            self.collection_buttons.append(button)

        self.play_button = Button(25, Config.get_window_height() - 125, 250, 100, "Play", 70, 0, 0, 20, 5, font_art="Calibri")
        self.globe_img = Utils.load_image("Other_Images/Globe")
        self.loading_text = py.font.SysFont("Calibri", 60, True).render("Assets are being loaded...", False, (255, 255, 255))

    def tick(self):
        self.current_state.tick()

        for i, b in enumerate(self.collection_buttons):
            if b.is_clicked():
                if not self.current_state == self.collection_state:
                    self.current_state = self.collection_state

                self.swtich_collection(i)

        if self.play_button.is_clicked() and Assets.FINISHED_LOADING:
            selected_categories = self.collection_state.get_selected_categories()

            if selected_categories: # If list isn't empty
                State.switch_state(self.main.get_game_state())

                self.main.game_state.load_cards(selected_categories, self.collection_state.include_map_checkbox.selected)

    def render(self, win):
        win.fill((46, 140, 230))

        self.current_state.render(win)

        self.play_button.render(win)

        py.draw.rect(win, (255, 255, 255), (300, 0, 5, Config.get_window_height()))

        for b in self.collection_buttons:
            b.render(win)

        win.blit(self.globe_img, (25, 25))

        if not Assets.FINISHED_LOADING:
            win.blit(self.loading_text, (1270, 1025))

    def swtich_collection(self, index: int) -> None:
        if index == self.collection_state.current_collection:
            self.collection_buttons[index].color_border = self.NORMAL_BUTTON_COLOR
            self.collection_state.current_collection = -1
            return
        
        self.collection_buttons[self.collection_state.current_collection].color_border = self.NORMAL_BUTTON_COLOR
        
        self.collection_buttons[index].color_border = self.HIGHLIGHT_BUTTON_COLOR
        self.collection_state.current_collection = index
