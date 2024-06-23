from __future__ import annotations
from scr.buttons.ButtonControl import ButtonControl
from scr.buttons.Category import Category

import pygame as py

class CategoryCollection(ButtonControl):
    def __init__(self, x, y, width, height, display_text, categories: list[Category], color=(255, 255, 255), colorB=(0, 0, 0), colorT=(0, 0, 0), font_size=30, offset_x=10, offset_y=10, border_size=3, img=None):
        super().__init__(x, y, width, height, display_text, color, colorB, colorT, font_size, offset_x, offset_y, border_size, img)
        self.categories = categories

        self.text = self.category_name if not display_text else display_text

    def click_action(self):
        if self.categories[0].selected:
            for c in self.categories:
                c.selected = False
        else:
            for c in self.categories:
                c.selected = True

    def render_selected(self):
        pass
    