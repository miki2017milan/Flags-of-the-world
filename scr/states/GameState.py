import pygame as py
import random

from logging import warn

from scr.states.State import State
from scr.Assets import Assets

class GameState(State):
    def __init__(self, main):
        super().__init__(main)

        self.cards = []
        self.current_card = 0
        self.can_space = True
        self.max_mode = 1

    def load_cards(self, selected_categories: set[str], include_map: bool) -> None:
        cards = set() # No duplicates
        for category in selected_categories:
            for card in Assets.CATEGORIES[category]["Countries"]:
                try:
                    cards.add(Assets.FLAGS[card])
                except KeyError:
                    warn(f"Flagge '{card}' konnte nicht zum spiel hinzugefügt werden da es ein Fehler beim Laden der Karte gab!")

        if len(cards) == 0:
            self.back()
            return

        self.cards = list(cards) 
        random.shuffle(self.cards)

        self.max_mode = 2 if include_map else 1 # 2 = include map

    def back(self) -> None:
        self.current_card = 0
        self.cards = []
        State.switch_state(self.main.get_menu_state())

    def tick(self):
        keys = py.key.get_pressed()

        if keys[py.K_BACKSPACE]:
            self.back()
            return

        if self.can_space and keys[py.K_SPACE]:
            self.can_space = False

            self.cards[self.current_card].mode += 1

            if self.cards[self.current_card].mode > self.max_mode:
                self.cards[self.current_card].mode = 0

                self.current_card += 1
                if self.current_card >= len(self.cards):
                    self.back()
                    return
        
        if not keys[py.K_SPACE]:
            self.can_space = True

    def render(self, win):
        win.fill((33, 33, 33))

        self.cards[self.current_card].render(win)

