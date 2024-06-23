import pygame as py
import random
from scr.states.State import State
from scr.Assets import Assets

class GameState(State):
    def __init__(self, main):
        super().__init__(main)

        self.cards = []
        self.current_card = 0
        self.can_space = True

    def load_cards(self, selected_categories: set[str]) -> None:
        cards = set() # No duplicates
        for c in selected_categories:
            for card in Assets.CATEGORIES[c]:
                try:
                    cards.add(Assets.FLAGS[card])
                except KeyError:
                    print(f"ADD ERROR: Flagge '{card}' konnte nicht zum spiel hinzugefügt werden da es ein Fehler beim Laden der Karte gab!")

        self.cards = list(cards) 
        random.shuffle(self.cards)

        if len(self.cards) == 0:
            self.back()

    def back(self) -> None:
        self.current_card = 0
        self.cards = []
        State.switch_state(self.main.menu_state)

    def tick(self):
        keys = py.key.get_pressed()

        if self.can_space and keys[py.K_SPACE]:
            self.can_space = False

            if self.cards[self.current_card].revealed:
                self.cards[self.current_card].revealed = False
                self.current_card += 1
                if self.current_card >= len(self.cards):
                    self.back()
            else:
                self.cards[self.current_card].revealed = True
        
        if not keys[py.K_SPACE]:
            self.can_space = True
            

    def render(self, win):
        win.fill((33, 33, 33))

        self.cards[self.current_card].render(win)

