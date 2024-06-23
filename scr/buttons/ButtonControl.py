import pygame as py

from abc import ABC, abstractmethod

class ButtonControl(ABC):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, color: tuple[int, int, int]=(255, 255, 255), colorB: tuple[int, int, int]=(0, 0, 0), colorT: tuple[int, int, int]=(0, 0, 0), font_size: int=30, offset_x: int=10, offset_y: int=10, border_size: int=3, img: py.surface.Surface=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.colorB = colorB
        self.colorT = colorT
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.img = img
        if img:
            self.img = py.transform.scale(img, (width, height))

        self.can_click = False
        self.BORDER_SIZE = border_size

        self.font = py.font.SysFont("Calibri", font_size, True)

    def is_clicked(self) -> bool:
        mx, my = py.mouse.get_pos()

        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height and self.can_click and py.mouse.get_pressed()[0]:
            return True
        return False
    
    def tick(self):
        if not py.mouse.get_pressed()[0]:
            self.can_click = True

        if self.is_clicked():
            self.can_click = False
            return self.click_action()

    def render(self, win: py.surface.Surface) -> None:
        if not self.img:
            py.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0, self.BORDER_SIZE)
            py.draw.rect(win, self.colorB, (self.x, self.y, self.width, self.height), 5, self.BORDER_SIZE)
        else:
            win.blit(self.img, (self.x, self.y))

        win.blit(self.font.render(self.text, False, self.colorT), (self.x + self.offset_x, self.y + self.offset_y))

    @abstractmethod
    def render_selected(self, win: py.surface.Surface) -> None:
        pass

    @abstractmethod
    def click_action(self):
        pass