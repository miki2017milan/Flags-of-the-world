import pygame as py

from scr.states.State import State
from scr.utils import Utils

from scr.buttons.BasicButton import BasicButton
from scr.buttons.Category import Category
from scr.buttons.CategoryCollection import CategoryCollection
from scr.buttons.CheckBox import CheckBox

class MenuState(State):
    def __init__(self, main):
        super().__init__(main)

        self.categories = [Category(335, 10, 200, 200, "Europe", img=Utils.load_image("Europe"), colorT=(255, 255, 255), offset_y=200, offset_x=55),
                           Category(565, 10, 200, 200, "North_Latein_America", "North America", img=Utils.load_image("NorthAmerica"), colorT=(255, 255, 255), offset_y=200),
                           Category(795, 10, 200, 200, "South_America", "South America", img=Utils.load_image("SouthAmerica"), colorT=(255, 255, 255), offset_y=200),
                           Category(335, 240, 200, 200, "Africa", img=Utils.load_image("Africa"), colorT=(255, 255, 255), offset_y=200, offset_x=60),
                           Category(565, 240, 200, 200, "Asia", img=Utils.load_image("Asia"), colorT=(255, 255, 255), offset_y=200, offset_x=75),
                           Category(795, 240, 200, 200, "Oceania", img=Utils.load_image("Oceania"), colorT=(255, 255, 255), offset_y=200, offset_x=50),
                           Category(335, 470, 200, 200, "Test"),
                           #Category(250, 365, 200, 200, "Other")
                           ]
        
        self.collection = [CategoryCollection(25, 300, 250, 160, "United Nations", self.categories[0:6], img=Utils.load_image("UN"), colorT=(255, 255, 255), offset_y=165, offset_x=30)]

        self.play_button = BasicButton(0, 899, 300, 125, "Play", border_size=0, offset_x=70, offset_y=25, font_size=80, colorB=(255, 255, 255))
        self.include_map_checkbox = CheckBox(325, 924, 75, 75, "Include maps", offset_x=0, offset_y=75)

        self.globe_img = Utils.load_image("Globe")

    def tick(self):
        for c in self.categories:
            c.tick()

        for c in self.collection:
            c.tick()

        self.include_map_checkbox.tick()

        if self.play_button.tick():
            selected_categories = [] # Using a set because order is irrelevant and duplicates aren't wished for

            # Add all categories
            for c in self.categories:
                if c.get_selected():
                    selected_categories.append(c.category_name)

            if selected_categories: # If list isn't empty
                State.switch_state(self.main.get_game_state())

                self.main.game_state.load_cards(selected_categories, self.include_map_checkbox.is_checked())

                for c in self.categories:
                    c.set_selected(False)

    def render(self, win):
        win.fill((46, 140, 230))

        self.play_button.render(win)
        self.include_map_checkbox.render(win)

        for c in self.categories:
            c.render(win)

        for c in self.collection:
            c.render(win)

        py.draw.rect(win, (255, 255, 255), (300, 0, 5, 1024))

        win.blit(self.globe_img, (25, 25))

