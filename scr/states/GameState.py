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

    def load_cards(self, selected_cards: set[str]) -> None:
        for c in selected_cards:
            self.cards.append(Assets.FLAGS[c])
        
        random.shuffle(self.cards)

    def back(self) -> None:
        State.switch_state(self.main.menu_state)
        self.current_card = 0
        self.cards = []

    def tick(self):
        keys = py.key.get_pressed()

        # for c in self.cards:
        #     print(c.name, end=", ")
        # print()

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

