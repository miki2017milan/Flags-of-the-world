import pygame as py
py.init()

from scr.states.State import State
from scr.utils import Utils, Config
from scr.Assets import Assets

from scr.buttons.Category import Category
from scr.buttons.CategoryCollection import CategoryCollection

from gui.CheckBox import CheckBox
from gui.Button import Button

class MenuState(State):
    def __init__(self, main):
        super().__init__(main)

        self.categories = [Category(335, 10, "Europe", Utils.load_image("Europe"), "Europe"),
                           Category(565, 10, "North_Latein_America", Utils.load_image("NorthAmerica"), "North America"),
                           Category(795, 10, "South_America", Utils.load_image("SouthAmerica"), "South America"),
                           Category(335, 240, "Africa", Utils.load_image("Africa"), "Africa"),
                           Category(565, 240, "Asia", Utils.load_image("Asia"), "Asia"),
                           Category(795, 240, "Oceania", Utils.load_image("Oceania"), "Oceania")
                           ]
        
        self.collection = [CategoryCollection(25, 300, 250, 160, self.categories[0:6], Utils.load_image("UN"), "United Nations")]

        self.play_button = Button(25, Config.get_window_height() - 125, 250, 100, "Play", 70, 65, 20, 20, 5, font_art="Calibri")
        self.include_map_checkbox = CheckBox(325, Config.get_window_height() - 112, 75, "Include maps", 30, 0, 75, font_art="Calibri")

        self.globe_img = Utils.load_image("Globe")

        self.loading_text = py.font.SysFont("Calibri", 60, True).render("Assets are being loaded...", False, (255, 255, 255))

    def tick(self):
        for c in self.categories:
            c.tick()

        for c in self.collection:
            c.tick()

        self.include_map_checkbox.tick()

        if self.play_button.is_clicked():
            selected_categories = [] # Using a set because order is irrelevant and duplicates aren't wished for

            # Add all categories
            for c in self.categories:
                if c.selected:
                    selected_categories.append(c.category_name)

            if selected_categories: # If list isn't empty
                State.switch_state(self.main.get_game_state())

                self.main.game_state.load_cards(selected_categories, self.include_map_checkbox.is_checked())

                for c in self.categories:
                    c.selected = False 

    def render(self, win):
        win.fill((46, 140, 230))

        self.play_button.render(win)
        self.include_map_checkbox.render(win)

        for c in self.categories:
            c.render(win)

        for c in self.collection:
            c.render(win)

        py.draw.rect(win, (255, 255, 255), (300, 0, 5, Config.get_window_height()))

        win.blit(self.globe_img, (25, 25))

        if not Assets.FINISHED_LOADING:
            win.blit(self.loading_text, (1270, 1025))

