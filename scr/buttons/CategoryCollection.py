from __future__ import annotations
from scr.buttons.ButtonControl import ButtonControl
from scr.buttons.Category import Category

import pygame as py

class CategoryCollection(ButtonControl):
    def __init__(self, x: int, y: int, width: int, height: int, display_text: str, categories: list[Category], color: tuple[int, int, int]=(255, 255, 255), colorB: tuple[int, int, int]=(0, 0, 0), colorT: tuple[int, int, int]=(0, 0, 0), font_size: int=30, offset_x: int=10, offset_y: int=10, border_size: int=3, img: py.surface.Surface | None=None):
        super().__init__(x, y, width, height, display_text, color, colorB, colorT, font_size, offset_x, offset_y, border_size, img)
        self.categories = categories

    def click_action(self) -> None:
        if self.categories[0].selected:
            for c in self.categories:
                c.selected = False
        else:
            for c in self.categories:
                c.selected = True

    def render_selected(self, win: py.surface.Surface) -> None:
        pass
    