from scr.states.State import State
from scr.Category import Category
from scr.Assets import Assets
from scr.Button import Button

class MenuState(State):
    def __init__(self, main):
        super().__init__(main)

        self.categories = [Category(10, 280, 200, 70, "United Nations", Assets.UN_STATES),
                           Category(10, 355, 200, 70, "Europe", Assets.EUROPE),
                           Category(10, 430, 200, 70, "North America", Assets.NORTH_LATIN_AMERICA),
                           Category(10, 505, 200, 70, "South America", Assets.SOUTH_AMERICA),
                           Category(10, 580, 200, 70, "Africa", Assets.AFRICA),
                           Category(10, 655, 200, 70, "Asia", Assets.ASIA),
                           Category(10, 730, 200, 70, "Oceania", Assets.OCEANIA),
                           Category(10, 805, 200, 70, "Other", Assets.OTHER),
                           Category(250, 280, 200, 70, "Test", Assets.TEST)]

        self.play_button = Button(235, 900, 250, 70, "Play", (200, 200, 200), (255, 255, 100))

    def tick(self):
        for c in self.categories:
            c.tick()

        if self.play_button.is_clicked():
            selected_cards = set() # Using a set because order is irrelevant and duplicates aren't wished for

            # Add all cards from selected categories
            for c in self.categories:
                if c.selected:
                    for card in c.cards:
                        selected_cards.add(card)

            if selected_cards: # If set isn't empty
                State.switch_state(self.main.game_state)

                self.main.game_state.load_cards(selected_cards)

                for c in self.categories:
                    c.selected = False

    def render(self, win):
        win.fill((46, 140, 230))

        self.play_button.render(win)

        for c in self.categories:
            c.render(win)

        win.blit(Assets.GLOBE_IMG, (235, 10))

