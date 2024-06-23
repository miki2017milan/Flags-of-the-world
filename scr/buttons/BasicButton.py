import pygame as py
from scr.buttons.ButtonControl import ButtonControl

class BasicButton(ButtonControl):
    def __init__(self, x, y, width, height, text, color=(255, 255, 255), colorB=(0, 0, 0), colorT=(0, 0, 0), font_size=30, offset_x=10, offset_y=10, border_size=3, img=None):
        super().__init__(x, y, width, height, text, color, colorB, colorT, font_size, offset_x, offset_y, border_size, img)

    def click_action(self):
        return True
    
    def render_selected(self, win) -> None:
        pass