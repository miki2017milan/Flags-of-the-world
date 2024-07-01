from __future__ import annotations

from scr.category.Category import Category
from gui.ImageButton import ImageButton
from scr.utils import Utils

import pygame as py

class CategoryCollection:
    def __init__(self, categories: list[str]):
        self.categories = []

        start_pos = (325, 10)
        increments = (230, 230)
        row = -1
        for i, c in enumerate(categories):
            if i % 7 == 0:
                row += 1
            self.categories.append(Category(start_pos[0] + increments[0] * (i % 7), start_pos[1] + increments[1] * row, c))

    def tick(self) -> None:
        for c in self.categories:
            c.tick()

    def render(self, win: py.surface.Surface) -> None:
        for c in self.categories:
            c.render(win)
    