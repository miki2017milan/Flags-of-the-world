import pygame as py

from .Label import Label
from typing import Iterable

class ImageButton:
    def __init__(self, x: int, y: int, img: py.surface.Surface, width: int=0, height: int=0, text: str="", font_size: int=20, text_offset_x: int=10, text_offset_y: int=10, color_text: tuple[int, int, int]=(0, 0, 0), font_art: str="Consolas"):
        self._x = x
        self._y = y
        self._img = img
        
        if width and height:
            self._width = width
            self._height = height
            self._img = py.transform.scale(img, (width, height))
        else:
            self._width = img.get_width()
            self._height = img.get_height()

        self._has_text = False
        if text:
            self._text = Label(x + text_offset_x, y + text_offset_y, text, font_size, color_text, font_art)
            self._has_text = True

        self._can_click = True

    def render(self, win: py.surface.Surface) -> None:
        win.blit(self.img, (self.x, self.y))

        if self._has_text:
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
        if self._has_text:
            self._text.x = int(self.x + ((self.width - self._text.get_width()) / 2))

    def center_text_y(self) -> None:
        if self._has_text:
            self._text.y = int(self.y + ((self.height - self._text.get_height()) / 2))

    @property
    def x(self) -> int:
        return self._x
    
    @x.setter
    def x(self, value: int):
        if not isinstance(value, int):
            raise TypeError("x must be of type 'int'")
        self._x = value

    @property
    def y(self) -> int:
        return self._y
    
    @y.setter
    def y(self, value: int):
        if not isinstance(value, int):
            raise TypeError("y must be of type 'int'")
        self._y = value

    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("width must be of type 'int' and greater 0")
        self._width = value
        self._img = py.transform.scale(self.img, (value, self.height))

    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("height must be of type 'int' and greater 0")
        self._height = value
        self._img = py.transform.scale(self.img, (self.width, value))

    @property
    def img(self) -> py.surface.Surface:
        return self._img
    
    @img.setter
    def img(self, value: py.surface.Surface):
        if not isinstance(value, py.surface.Surface):
            raise TypeError("img must be of type 'py.surface.Surface'")
        self._img = value

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