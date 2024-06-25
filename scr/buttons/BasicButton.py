import pygame as py
from scr.buttons.ButtonControl import ButtonControl

class BasicButton(ButtonControl):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, color: tuple[int, int, int]=(255, 255, 255), colorB: tuple[int, int, int]=(0, 0, 0), colorT: tuple[int, int, int]=(0, 0, 0), font_size: int=30, offset_x: int=10, offset_y: int=10, border_size: int=3, img: py.surface.Surface=None):
        super().__init__(x, y, width, height, text, color, colorB, colorT, font_size, offset_x, offset_y, border_size, img)

    def click_action(self) -> bool:
        return True
    
    def render_selected(self, win: py.surface.Surface) -> None:
        pass