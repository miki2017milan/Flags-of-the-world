import pygame as py

class ImageDisplay:
    def __init__(self, img: py.surface.Surface, x: int, y: int, width: int=0, height: int=0):
        self._img = img
        self._x = x
        self._y = y

        if width and height:
            self._width = width
            self._height = height
            self._img = py.transform.scale(img, (width, height))
        else:
            self._width = img.get_width()
            self._height = img.get_height()

    def render(self, win: py.surface.Surface) -> None:
        win.blit(self.img, (self.x, self.y, self.width, self.height))

    @property
    def img(self) -> py.surface.Surface:
        return self._img
    
    @img.setter
    def img(self, value: py.surface.Surface):
        if not isinstance(value, py.surface.Surface):
            raise TypeError("img must be of type 'py.surface.Surface'")
        self._img = value

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