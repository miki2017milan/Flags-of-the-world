import pygame as py

from scr.states.State import State

from scr.utils import Utils, Config
from scr.Assets import Assets

from scr.category.CategoryCollection import CategoryCollection

from gui.CheckBox import CheckBox
from gui.Button import Button

class CollectionState(State):
    def __init__(self, main):
        super().__init__(main)

        self.collections = []
        for k in Assets.COLLECTIONS.keys():
            self.collections.append(CategoryCollection(k))

        self.current_collection = -1
        self.currently_selected_cards = 0

        self.select_all_button = Button(325, Config.get_window_height() - 112, 225, 75, "Select all", 40, 0, 0, 20, 5, font_art="Calibri")
        self.include_map_checkbox = CheckBox(575, Config.get_window_height() - 112, 75, "Include maps", 30, -30, 75, font_art="Calibri")

        self.select_category_text = py.font.SysFont("Calibri", 60, True).render("Select one of the categories on the left", False, (255, 255, 255))

    def tick(self):
        if self.current_collection < 0:
            return
        
        self.include_map_checkbox.tick()
        self.collections[self.current_collection].tick()
        
        self.select_all_functionality()

        self.calculate_selected_cards()

    def render(self, win):
        win.blit(py.font.SysFont("Calibri", 40, True).render(f"Selected", False, (255, 255, 255)), (25, 870))
        win.blit(py.font.SysFont("Calibri", 40, True).render(f"cards: {self.currently_selected_cards}", False, (255, 255, 255)), (25, 900))

        if self.current_collection < 0:
             win.blit(self.select_category_text, (600, 500))
             return
        
        self.collections[self.current_collection].render(win)
        self.select_all_button.render(win)
        self.include_map_checkbox.render(win)

    def select_all_functionality(self):
        if self.select_all_button.is_clicked():
            if self.all_selected():
                for category in self.collections[self.current_collection].categories:
                    category.selected = False
                return

            for category in self.collections[self.current_collection].categories:
                category.selected = True

        if self.all_selected():
            if not self.select_all_button.text == "Unselect all":
                self.select_all_button.text = "Unselect all"
                self.select_all_button.center_text_x()
        else:
            if not self.select_all_button.text == "Select all":
                self.select_all_button.text = "Select all"
                self.select_all_button.center_text_x()

    def calculate_selected_cards(self):
        self.currently_selected_cards = 0
        for collection in self.collections:
            for category in collection.categories:
                if category.selected:
                    self.currently_selected_cards += category.get_card_count()

    def all_selected(self):
        for category in self.collections[self.current_collection].categories:
            if not category.selected:
                return False
                
        return True
    
    def get_selected_categories(self) -> list[str]:
        selected_categories = []

        for collection in self.collections:
            for category in collection.categories:
                if category.selected:
                    selected_categories.append(category.category_name)

        return selected_categories