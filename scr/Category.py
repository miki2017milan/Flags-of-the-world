from __future__ import annotations

import pygame as py

# category height = 70

class Category:
    def __init__(self, x: int, y: int, width: int, height: int, category_name: str, display_name: str=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.category_name = category_name

        if not display_name:
            self.display_name = self.category_name
        else:
            self.display_name = display_name
        
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
        win.blit(self.font.render(self.display_name, False, (0, 0, 0)), (self.x + 10, self.y + 10))

        if self.selected:
            py.draw.rect(win, (255, 255, 100), (self.x, self.y, self.width, self.height), 5, self.BORDER_RADIUS)
    