import pygame as py
py.init()

from scr.states.State import State
from scr.utils import Utils, Config
from scr.Assets import Assets

from scr.category.Category import Category
from scr.category.CategoryCollection import CategoryCollection

from gui.CheckBox import CheckBox
from gui.Button import Button

class MenuState(State):
    def __init__(self, main):
        super().__init__(main)

        self.nation_collection = CategoryCollection(("Europe", "North America", "South America", "Africa", "Asia", "Oceania", "Test", "Other"))
        self.selected_collection = self.nation_collection

        self.play_button = Button(25, Config.get_window_height() - 125, 250, 100, "Play", 70, 65, 20, 20, 5, font_art="Calibri")
        self.include_map_checkbox = CheckBox(325, Config.get_window_height() - 112, 75, "Include maps", 30, 0, 75, font_art="Calibri")

        self.globe_img = Utils.load_image("Globe")

        self.loading_text = py.font.SysFont("Calibri", 60, True).render("Assets are being loaded...", False, (255, 255, 255))

    def tick(self):
        self.selected_collection.tick()

        self.include_map_checkbox.tick()

        if self.play_button.is_clicked() and Assets.FINISHED_LOADING:
            selected_categories = []

            # Add all selected categories
            for c in self.selected_collection.categories:
                if c.selected:
                    selected_categories.append(c.category_name)

            if selected_categories: # If list isn't empty
                State.switch_state(self.main.get_game_state())

                self.main.game_state.load_cards(selected_categories, self.include_map_checkbox.selected)

                for c in self.selected_collection.categories:
                    c.selected = False 

    def render(self, win):
        win.fill((46, 140, 230))

        self.play_button.render(win)
        self.include_map_checkbox.render(win)

        self.selected_collection.render(win)

        py.draw.rect(win, (255, 255, 255), (300, 0, 5, Config.get_window_height()))

        win.blit(self.globe_img, (25, 25))

        if not Assets.FINISHED_LOADING:
            win.blit(self.loading_text, (1270, 1025))

