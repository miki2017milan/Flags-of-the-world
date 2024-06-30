from __future__ import annotations

from gui.ImageButton import ImageButton

import pygame as py

class Category(ImageButton):
    def __init__(self, x: int, y: int, category_name: str, img: py.surface.Surface, display_text):
        super().__init__(x, y, img, 200, 200, display_text, 30, 0, 200, (255, 255, 255), "Calibri")
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
    