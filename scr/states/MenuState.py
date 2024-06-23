import pygame as py

from scr.states.State import State
from scr.Assets import Assets

from scr.buttons.BasicButton import BasicButton
from scr.buttons.Category import Category
from scr.buttons.CategoryCollection import CategoryCollection

class MenuState(State):
    def __init__(self, main):
        super().__init__(main)

        self.categories = [Category(335, 10, 200, 200, "Europe", img=Assets.EUROPE_BUTTON, colorT=(255, 255, 255), offset_y=200, offset_x=55),
                           Category(565, 10, 200, 200, "North_Latein_America", "North America", img=Assets.NORTH_AMERICA_BUTTON, colorT=(255, 255, 255), offset_y=200),
                           Category(795, 10, 200, 200, "South_America", "South America", img=Assets.SOUTH_AMERICA_BUTTON, colorT=(255, 255, 255), offset_y=200),
                           Category(335, 240, 200, 200, "Africa", img=Assets.AFRICA_BUTTON, colorT=(255, 255, 255), offset_y=200, offset_x=60),
                           Category(565, 240, 200, 200, "Asia", img=Assets.ASIA_BUTTON, colorT=(255, 255, 255), offset_y=200, offset_x=75),
                           Category(795, 240, 200, 200, "Oceania", img=Assets.OCEANIA_BUTTON, colorT=(255, 255, 255), offset_y=200, offset_x=50),
                           #Category(250, 280, 200, 200, "Other"),
                           #Category(250, 365, 200, 200, "Test")
                           ]
        
        self.collection = [CategoryCollection(25, 300, 250, 160, "United Nations", self.categories[0:6], img=Assets.UN_BUTTON, colorT=(255, 255, 255), offset_y=165, offset_x=30)]

        self.play_button = BasicButton(25, 899, 250, 100, "Play", border_size=30, offset_x=55, offset_y=15, font_size=80)

    def tick(self):
        for c in self.categories:
            c.tick()

        for c in self.collection:
            c.tick()

        if self.play_button.tick():
            selected_categories = [] # Using a set because order is irrelevant and duplicates aren't wished for

            # Add all categories
            for c in self.categories:
                if c.selected:
                    selected_categories.append(c.category_name)

            if selected_categories: # If list isn't empty
                State.switch_state(self.main.game_state)

                self.main.game_state.load_cards(selected_categories)

                for c in self.categories:
                    c.selected = False

    def render(self, win):
        win.fill((46, 140, 230))

        self.play_button.render(win)

        for c in self.categories:
            c.render(win)

        for c in self.collection:
            c.render(win)

        py.draw.rect(win, (255, 255, 255), (300, 0, 5, 1024))

        win.blit(Assets.GLOBE_IMG, (25, 25))

