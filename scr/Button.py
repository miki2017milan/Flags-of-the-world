import pygame as py

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, color: tuple[int, int, int]=(255, 255, 255), colorB: tuple[int, int, int]=(0, 0, 0), colorT: tuple[int, int, int]=(0, 0, 0), font_size: int=30, offset_x: int=10, offset_y: int=10):
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

        self.can_click = False

        self.font = py.font.SysFont("Calibri", font_size, True)

    def is_clicked(self) -> bool:
        mx, my = py.mouse.get_pos()

        if not py.mouse.get_pressed()[0]:
            self.can_click = True

        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height and self.can_click and py.mouse.get_pressed()[0]:
            self.can_click = False
            return True
        return False

    def render(self, win: py.surface.Surface) -> None:
        py.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0, 3)
        py.draw.rect(win, self.colorB, (self.x, self.y, self.width, self.height), 5, 3)

        win.blit(self.font.render(self.text, False, self.colorT), (self.x + self.offset_x, self.y + self.offset_y))
