from __future__ import annotations

from scr.category.Category import Category
from scr.Assets import Assets

import pygame as py

class CategoryCollection:
    def __init__(self, collection_name: str):
        self.categories = []

        start_pos = (325, 10)
        increments = (230, 230)
        row = -1
        for i, c in enumerate(Assets.COLLECTIONS[collection_name]):
            if i % 7 == 0:
                row += 1
            self.categories.append(Category(start_pos[0] + increments[0] * (i % 7), start_pos[1] + increments[1] * row, c, collection_name))

    def tick(self) -> None:
        for c in self.categories:
            c.tick()

    def render(self, win: py.surface.Surface) -> None:
        for c in self.categories:
            c.render(win)
    