import pygame as py

from typing import Iterable

class Label:
    def __init__(self, x: int, y: int, text: str, font_size: int, color_text: tuple[int, int, int]=(255, 255, 255), font_art: str="Consolas"):
        self._x = x
        self._y = y
        self._text = text
        self._color_text = color_text
        self._font_art = font_art
        self._font_size = font_size
        self._visible = True
        
        self.create_text_surface()

    def render(self, win: py.surface.Surface) -> None:
        if self.visible:
            win.blit(self._text_surface, (self.x, self.y))

    def create_text_surface(self):
        self._font = py.font.SysFont(self.font_art, self.font_size, True)
        self._text_surface = self._font.render(self.text, False, self.color_text)
    
    # Getter Setter
    def get_width(self) -> int:
        return self._text_surface.get_width()
    
    def get_height(self) -> int:
        return self._text_surface.get_height()

    @property
    def color_text(self) -> tuple[int, int, int]:
        return self._color_text
    
    @color_text.setter
    def color_text(self, value: tuple[int, int, int]):
        if not isinstance(value, Iterable):
            raise TypeError("color_text must be a tuple in rgb format")
        self._color_text = value
        self.create_text_surface()

    @property
    def font_size(self) -> int:
        return self._font_size
    
    @font_size.setter
    def font_size(self, value: int):
        if not isinstance(value, int):
            raise TypeError("font_size must be of type 'int'")
        self._font_size = value
        self.create_text_surface()

    @property
    def font_art(self) -> str:
        return self._font_art
    
    @font_art.setter
    def font_art(self, value: str):
        if not isinstance(value, str):
            raise TypeError("font_art must be of type 'str'")
        self._font_art = value
        self.create_text_surface()

    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str):
        if not isinstance(value, str):
            raise TypeError("text must be of type 'str'")
        self._text = value
        self.create_text_surface()

    @property
    def visible(self) -> bool:
        return self._visible
    
    @visible.setter
    def visible(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("visible must be of type 'bool'")
        self._visible = value

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