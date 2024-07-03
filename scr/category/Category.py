from __future__ import annotations

import pygame as py

from os.path import join

from gui.ImageButton import ImageButton
from scr.Assets import Assets
from scr.utils import Utils

class Category(ImageButton):
    def __init__(self, x: int, y: int, category_name: str, collection_name: str):
        super().__init__(x, y, Utils.load_image(join(Utils.CATEGORIES_PATH, collection_name, category_name, "Icon")), 200, 200, category_name, 30, 0, 200, (255, 255, 255), "Calibri")
        self.category_name = category_name

        self.center_text_x()

        self.selected = False

    def render(self, win: py.surface.Surface) -> None:
        super().render(win)

        if self.selected:
            py.draw.rect(win, (255, 255, 100), (self.x, self.y, self.width, self.height), 5, 5)

    def tick(self) -> None:
        if self.is_clicked():
            self.selected = not self.selected

    def get_card_count(self) -> int:
        return len(Assets.CATEGORIES[self.category_name]["Countries"])
    