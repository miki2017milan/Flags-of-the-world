from __future__ import annotations

from scr.buttons.Category import Category
from gui.ImageButton import ImageButton

import pygame as py

class CategoryCollection(ImageButton):
    def __init__(self, x: int, y: int, width: int, height: int, categories: list[Category], img: py.surface.Surface, display_text):
        super().__init__(x, y, img, width, height, display_text, 30, 0, 200, (255, 255, 255), "Calibri")
        self.categories = categories

        self.center_text_x()

        self.selected = False

    def tick(self):
        if self.is_clicked():
            if self.categories[0].selected:
                for c in self.categories:
                    c.selected = False
                return
            for c in self.categories:
                c.selected = True
    