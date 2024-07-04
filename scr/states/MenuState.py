import pygame as py
py.init()

from scr.states.State import State
from scr.utils import Utils, Config
from scr.Assets import Assets

from scr.category.CategoryCollection import CategoryCollection

from gui.CheckBox import CheckBox
from gui.Button import Button

class MenuState(State):
    def __init__(self, main):
        super().__init__(main)

        self.collections = []
        self.collection_buttons = []
        for i, (k, v) in enumerate(Assets.COLLECTIONS.items()):
            self.collections.append(CategoryCollection(k))
            self.collection_buttons.append(Button(25, 300 + 100 * i, 250, 80, k, 20, 10, 10, 20, 5, (26, 120, 210), (255, 255, 255), (255, 255, 255), font_art="Calibri"))

        for b in self.collection_buttons:
            b.center_text_x()
            b.center_text_y()

        self.current_collection = -1
        self.currently_selected_cards = 0

        self.play_button = Button(25, Config.get_window_height() - 125, 250, 100, "Play", 70, 0, 0, 20, 5, font_art="Calibri")
        self.select_all_button = Button(325, Config.get_window_height() - 112, 225, 75, "Select all", 40, 0, 0, 20, 5, font_art="Calibri")
        self.deselect_all_button = Button(575, Config.get_window_height() - 112, 225, 75, "Deselect all", 40, 65, 20, 20, 5, font_art="Calibri")
        self.include_map_checkbox = CheckBox(830, Config.get_window_height() - 112, 75, "Include maps", 30, -30, 75, font_art="Calibri")

        self.globe_img = Utils.load_image("Other_Images/Globe")

        self.loading_text = py.font.SysFont("Calibri", 60, True).render("Assets are being loaded...", False, (255, 255, 255))
        self.tutorial_text = py.font.SysFont("Calibri", 60, True).render("Select one of the categories on the left", False, (255, 255, 255))

    def tick(self):
        self.include_map_checkbox.tick()

        for i, b in enumerate(self.collection_buttons):
            if b.is_clicked():
                if i == self.current_collection:
                    self.swtich_collection(-1)
                    break
                self.swtich_collection(i)

        if self.play_button.is_clicked() and Assets.FINISHED_LOADING:
            selected_categories = []

            # Add all selected categories
            for collection in self.collections:
                for category in collection.categories:
                    if category.selected:
                        selected_categories.append(category.category_name)

            if selected_categories: # If list isn't empty
                State.switch_state(self.main.get_game_state())

                self.main.game_state.load_cards(selected_categories, self.include_map_checkbox.selected)

                for collection in self.collections:
                    for category in collection.categories:
                        category.selected = False

        if self.current_collection == -1:
            return
        
        self.collections[self.current_collection].tick()
        
        if self.select_all_button.is_clicked():
            for category in self.collections[self.current_collection].categories:
                category.selected = True

        if self.deselect_all_button.is_clicked():
            for category in self.collections[self.current_collection].categories:
                category.selected = False

        self.currently_selected_cards = 0
        for collection in self.collections:
            for category in collection.categories:
                if category.selected:
                    self.currently_selected_cards += category.get_card_count()

    def render(self, win):
        win.fill((46, 140, 230))

        self.play_button.render(win)
        self.select_all_button.render(win)
        self.deselect_all_button.render(win)
        self.include_map_checkbox.render(win)

        win.blit(py.font.SysFont("Calibri", 40, True).render(f"Selected", False, (255, 255, 255)), (25, 870))
        win.blit(py.font.SysFont("Calibri", 40, True).render(f"cards: {self.currently_selected_cards}", False, (255, 255, 255)), (25, 900))
        
        if self.current_collection >= 0:
            self.collections[self.current_collection].render(win)
        else:
            win.blit(self.tutorial_text, (600, 500))
        for b in self.collection_buttons:
            b.render(win)

        py.draw.rect(win, (255, 255, 255), (300, 0, 5, Config.get_window_height()))

        win.blit(self.globe_img, (25, 25))

        if not Assets.FINISHED_LOADING:
            win.blit(self.loading_text, (1270, 1025))

    def swtich_collection(self, index: int) -> None:
        if index == -1:
            self.collection_buttons[self.current_collection].color_border = (255, 255, 255)
            self.collection_buttons[self.current_collection].back = (26, 120, 210)
            self.current_collection = -1
            return

        self.collection_buttons[self.current_collection].color_border = (255, 255, 255)
        self.collection_buttons[self.current_collection].back = (26, 120, 210)
        
        self.collection_buttons[index].color_border = (130, 130, 130)
        self.collection_buttons[index].color_back = (6, 100, 190)

        self.current_collection = index
