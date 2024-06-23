from __future__ import annotations
from scr.buttons.ButtonControl import ButtonControl

import pygame as py

# category height = 70

class Category(ButtonControl):
    def __init__(self, x, y, width, height, category_name, display_text: str="", color=(255, 255, 255), colorB=(0, 0, 0), colorT=(0, 0, 0), font_size=30, offset_x=10, offset_y=10, border_size=3, img=None):
        super().__init__(x, y, width, height, display_text, color, colorB, colorT, font_size, offset_x, offset_y, border_size, img)
        self.category_name = category_name

        self.text = self.category_name if not display_text else display_text

        self.selected = False

    def render(self, win):
        super().render(win)

        if self.selected:
            self.render_selected(win)

    def click_action(self):
        self.selected = not self.selected

    def render_selected(self, win):
        py.draw.rect(win, (255, 255, 100), (self.x, self.y, self.width, self.height), 5, self.BORDER_SIZE)
    