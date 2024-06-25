import pygame as py
from scr.buttons.ButtonControl import ButtonControl

class CheckBox(ButtonControl):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, color: tuple[int, int, int]=(255, 255, 255), colorB: tuple[int, int, int]=(0, 0, 0), colorT: tuple[int, int, int]=(0, 0, 0), font_size: int=30, offset_x: int=10, offset_y: int=10, border_size: int=3):
        super().__init__(x, y, width, height, text, color, colorB, colorT, font_size, offset_x, offset_y, border_size, None)

        self.checked = False
        self.SELECTED_BOX_BUFFER = 10

    def render(self, win: py.Surface) -> None:
        super().render(win)

        if self.checked:
            py.draw.rect(win, self.colorB, (self.x + self.SELECTED_BOX_BUFFER, self.y + self.SELECTED_BOX_BUFFER, self.width - self.SELECTED_BOX_BUFFER * 2, self.height - self.SELECTED_BOX_BUFFER * 2))

    def click_action(self) -> None:
        self.checked = not self.checked

    def is_checked(self) -> bool:
        return self.checked