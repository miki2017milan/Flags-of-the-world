from __future__ import annotations
from collections import OrderedDict

import pygame as py

# category height = 70

class Category:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, cards: tuple[str, ...]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.cards = cards
        
        self.selected = False
        self.can_click = True

        self.BORDER_RADIUS = 3

        self.font = py.font.SysFont("Calibri", 30, True)

    def tick(self) -> None:
        mx, my = py.mouse.get_pos()

        if not py.mouse.get_pressed()[0]:
            self.can_click = True

        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height and self.can_click and py.mouse.get_pressed()[0]:
            self.can_click = False
            self.selected = not self.selected

    def render(self, win: py.surface.Surface) -> None:
        py.draw.rect(win, (46, 100, 160), (self.x, self.y, self.width, self.height), 0, self.BORDER_RADIUS)
        win.blit(self.font.render(self.text, False, (0, 0, 0)), (self.x + 10, self.y + 10))

        if self.selected:
            py.draw.rect(win, (255, 255, 100), (self.x, self.y, self.width, self.height), 5, self.BORDER_RADIUS)
    