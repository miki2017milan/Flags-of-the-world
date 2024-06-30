import pygame as py

from gui.Label import Label
from typing import Iterable

class CheckBox:
    def __init__(self, x: int, y: int, size: int, text: str="", font_size: int=20, text_offset_x: int=10, text_offset_y: int=10, corner_roundness: int=0, border_thickness: int=5, color_back: tuple[int, int, int]=(255, 255, 255), color_border: tuple[int, int, int]=(0, 0, 0), color_text: tuple[int, int, int]=(0, 0, 0), font_art: str="Consolas"):
        self._x = x
        self._y = y
        self._size = size
        self._color_back = color_back
        self._color_border = color_border
        self._text_offset_x = text_offset_x
        self._text_offset_y = text_offset_y
        self._corner_roundness = corner_roundness
        self._border_thickness = border_thickness

        self._has_text = False
        if text:
            self._text = Label(x + text_offset_x, y + text_offset_y, text, font_size, color_text, font_art)
            self._has_text = True

        self._can_click = True
        self.selected = False

    def render(self, win: py.surface.Surface) -> None:
        py.draw.rect(win, self.color_back, (self.x, self.y, self.size, self.size), border_radius=self.corner_roundness)
        py.draw.rect(win, self.color_border, (self.x, self.y, self.size, self.size), self.border_thickness, self.corner_roundness)

        if self.selected:
            py.draw.rect(win, self.color_border, (self.x + self.border_thickness * 2, self.y + self.border_thickness * 2, self.size - self.border_thickness * 4, self.size - self.border_thickness * 4), border_radius=self.corner_roundness)

        if self._has_text:
            self._text.render(win)

    def tick(self) -> None:
        mx, my = py.mouse.get_pos()

        if not py.mouse.get_pressed()[0]:
            self._can_click = True

        if self.x < mx < self.x + self.size and self.y < my < self.y + self.size and self._can_click and py.mouse.get_pressed()[0]:
            self._can_click = False
            self.selected = not self.selected

    @property
    def selected(self) -> bool:
        return self._selected
    
    @selected.setter
    def selected(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("selected must be of type 'bool'")
        self._selected = value

    @property
    def x(self) -> int:
        return self._x
    
    @x.setter
    def x(self, value: int):
        if not isinstance(value, int):
            raise TypeError("x must be of type 'int'")
        self._x = value
        if self._has_text:
            self._text.x = value + self.text_offset_x

    @property
    def y(self) -> int:
        return self._y
    
    @y.setter
    def y(self, value: int):
        if not isinstance(value, int):
            raise TypeError("y must be of type 'int'")
        self._y = value
        if self._has_text:
            self._text.y = value + self.text_offset_y

    @property
    def size(self) -> int:
        return self._size
    
    @size.setter
    def size(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("size must be of type 'int' and greater 0")
        self._size = value

    @property
    def text_offset_x(self) -> int:
        return self._text_offset_x
    
    @text_offset_x.setter
    def text_offset_x(self, value: int):
        if not isinstance(value, int):
            raise TypeError("text_offset_x must be of type 'int'")
        self._text_offset_x = value
        if self._has_text:
            self._text.x = self.x + value

    @property
    def text_offset_y(self) -> int:
        return self._text_offset_y
    
    @text_offset_y.setter
    def text_offset_y(self, value: int):
        if not isinstance(value, int):
            raise TypeError("text_offset_y must be of type 'int'")
        self._text_offset_y = value
        if self._has_text:
            self._text.y = self.y + value

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
    def font_size(self) -> int | None:
        if self._has_text:
            return self._text.font_size
        return None
    
    @font_size.setter
    def font_size(self, value: int):
        if not isinstance(value, int):
            raise TypeError("font_size must be of type 'int'")
        if self._has_text:
            self._text.font_size = value

    @property
    def font_art(self) -> str:
        return self._text.font_art
    
    @font_art.setter
    def font_art(self, value: str):
        if not isinstance(value, str):
            raise TypeError("font_art must be of type 'str'")
        if self._has_text:
            self._text.font_art = value

    @property
    def text(self) -> str:
        return self._text.text
    
    @text.setter
    def text(self, value: str):
        if not isinstance(value, str):
            raise TypeError("text must be of type 'str'")
        
        if self._has_text:
            self._text.text = value

    @property
    def color_text(self) -> tuple[int, int, int] | None:
        if self._has_text:
            return self._text.color_text
        return None
    @color_text.setter
    def color_text(self, value: tuple[int, int, int]):
        if not isinstance(value, Iterable):
            raise TypeError("color_text must be a tuple in rgb format")
        if self._has_text:
            self._text.color_text = value