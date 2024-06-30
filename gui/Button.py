import pygame as py

from gui.Label import Label
from typing import Iterable

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font_size: int, text_offset_x: int=10, text_offset_y: int=10, corner_roundness: int=0, border_thickness: int=5, color_back: tuple[int, int, int]=(255, 255, 255), color_border: tuple[int, int, int]=(0, 0, 0), color_text: tuple[int, int, int]=(0, 0, 0), font_art: str="Consolas"):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color_back = color_back
        self._color_border = color_border
        self._text_offset_x = text_offset_x
        self._text_offset_y = text_offset_y
        self._corner_roundness = corner_roundness
        self._border_thickness = border_thickness
        
        self._text = Label(x + text_offset_x, y + text_offset_y, text, font_size, color_text, font_art)

        self._can_click = True

    def render(self, win: py.surface.Surface) -> None:
        py.draw.rect(win, self.color_back, (self.x, self.y, self.width, self.height), border_radius=self.corner_roundness)
        py.draw.rect(win, self.color_border, (self.x, self.y, self.width, self.height), self.border_thickness, self.corner_roundness)

        self._text.render(win)

    def is_clicked(self) -> bool:
        mx, my = py.mouse.get_pos()

        if not py.mouse.get_pressed()[0]:
            self._can_click = True

        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height and self._can_click and py.mouse.get_pressed()[0]:
            self._can_click = False
            return True
        return False

    def center_text_x(self) -> None:
        self._text.x = int(self.x + ((self.width - self._text.get_width()) / 2))

    def center_text_y(self) -> None:
        self._text.y = int(self.y + ((self.height - self._text.get_height()) / 2))

    @property
    def x(self) -> int:
        return self._x
    
    @x.setter
    def x(self, value: int):
        if not isinstance(value, int):
            raise TypeError("x must be of type 'int'")
        self._x = value
        self._text.x = value + self.text_offset_x

    @property
    def y(self) -> int:
        return self._y
    
    @y.setter
    def y(self, value: int):
        if not isinstance(value, int):
            raise TypeError("y must be of type 'int'")
        self._y = value
        self._text.y = value + self.text_offset_y

    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("width must be of type 'int' and greater 0")
        self._width = value

    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("height must be of type 'int' and greater 0")
        self._height = value

    @property
    def color_back(self) -> tuple[int, int, int]:
        return self._color_back
    
    @color_back.setter
    def color_back(self, value: tuple[int, int, int]):
        if not isinstance(value, Iterable):
            raise TypeError("color_back must be a tuple in rgb format")
        self._color_back = value

    @property
    def color_border(self) -> tuple[int, int, int]:
        return self._color_border
    
    @color_border.setter
    def color_border(self, value:tuple[int, int, int] ):
        if not isinstance(value, Iterable):
            raise TypeError("color_border must be a tuple in rgb format")
        self._color_border = value

    @property
    def text_offset_x(self) -> int:
        return self._text_offset_x
    
    @text_offset_x.setter
    def text_offset_x(self, value: int):
        if not isinstance(value, int):
            raise TypeError("text_offset_x must be of type 'int'")
        self._text_offset_x = value
        self._text.x = self.x + value

    @property
    def text_offset_y(self) -> int:
        return self._text_offset_y
    
    @text_offset_y.setter
    def text_offset_y(self, value: int):
        if not isinstance(value, int):
            raise TypeError("text_offset_y must be of type 'int'")
        self._text_offset_y = value
        self._text.y = self.y + value

    @property
    def corner_roundness(self) -> int:
        return self._corner_roundness
    
    @corner_roundness.setter
    def corner_roundness(self, value: int):
        if not isinstance(value, int):
            raise TypeError("corner_roundness must be of type 'int'")
        self._corner_roundness = value

    @property
    def border_thickness(self) -> int:
        return self._border_thickness
    
    @border_thickness.setter
    def border_thickness(self, value: int):
        if not isinstance(value, int):
            raise TypeError("border_thickness must be of type 'int'")
        self._border_thickness = value
    
    @property
    def font_size(self) -> int:
        return self._text.font_size
    
    @font_size.setter
    def font_size(self, value: int):
        if not isinstance(value, int):
            raise TypeError("font_size must be of type 'int'")
        self._text.font_size = value

    @property
    def font_art(self) -> str:
        return self._text.font_art
    
    @font_art.setter
    def font_art(self, value: str):
        if not isinstance(value, str):
            raise TypeError("font_art must be of type 'str'")
        self._text.font_art = value

    @property
    def text(self) -> str:
        return self._text.text
    
    @text.setter
    def text(self, value: str):
        if not isinstance(value, str):
            raise TypeError("text must be of type 'str'")
        self._text.text = value

    @property
    def color_text(self) -> tuple[int, int, int]:
        return self._text.color_text
    
    @color_text.setter
    def color_text(self, value: tuple[int, int, int]):
        if not isinstance(value, Iterable):
            raise TypeError("color_text must be a tuple in rgb format")
        self._text.color_text = value