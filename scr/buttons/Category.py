from __future__ import annotations
from scr.buttons.ButtonControl import ButtonControl

import pygame as py

class Category(ButtonControl):
    def __init__(self, x: int, y: int, width: int, height: int, category_name: str, display_text: str="", color: tuple[int, int, int]=(255, 255, 255), colorB: tuple[int, int, int]=(0, 0, 0), colorT: tuple[int, int, int]=(0, 0, 0), font_size: int=30, offset_x: int=10, offset_y: int=10, border_size: int=3, img: py.surface.Surface=None):
        super().__init__(x, y, width, height, display_text, color, colorB, colorT, font_size, offset_x, offset_y, border_size, img)
        self.category_name = category_name

        self.text = self.category_name if not display_text else display_text

        self.selected = False

    def render(self, win: py.surface.Surface) -> None:
        super().render(win)

        if self.selected:
            py.draw.rect(win, (255, 255, 100), (self.x, self.y, self.width, self.height), 5, self.BORDER_SIZE)

    def click_action(self) -> None:
        self.selected = not self.selected

    def get_selected(self) -> bool:
        return self.selected
    
    def set_selected(self, value: bool):
        self.selected = value
    