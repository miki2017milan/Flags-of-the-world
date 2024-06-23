from scr.states.State import State
from scr.Category import Category
from scr.Assets import Assets
from scr.Button import Button

class MenuState(State):
    def __init__(self, main):
        super().__init__(main)

        self.categories = [Category(10, 280, 200, 70, "UN_States", "United Nations"),
                           Category(10, 355, 200, 70, "Europe"),
                           Category(10, 430, 200, 70, "North_Latein_America", "North America"),
                           Category(10, 505, 200, 70, "South_America", "South America"),
                           Category(10, 580, 200, 70, "Africa"),
                           Category(10, 655, 200, 70, "Asia"),
                           Category(10, 730, 200, 70, "Oceania"),
                           Category(10, 805, 200, 70, "Other"),
                           Category(250, 280, 200, 70, "Test")]

        self.play_button = Button(235, 900, 250, 70, "Play", (200, 200, 200), (255, 255, 100))

    def tick(self):
        for c in self.categories:
            c.tick()

        if self.play_button.is_clicked():
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

        win.blit(Assets.GLOBE_IMG, (235, 10))

