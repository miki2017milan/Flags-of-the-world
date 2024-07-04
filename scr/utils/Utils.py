import pygame as py
import json
import sys

from logging import warn
from os.path import join

from scr.utils import Config

RES_PATH = join(sys.path[0].replace("\\scr", ""), "res")
FLAG_PATH = join(RES_PATH, "Flags")
CATEGORIES_PATH = join(RES_PATH, "Collections")

def load_image(image_name: str) -> py.surface.Surface:
    return py.image.load(join(RES_PATH, image_name + ".png"))

def load_flag(flag_name: str) -> py.surface.Surface:
    return py.image.load(join(FLAG_PATH, flag_name, "Flag.png"))

def load_map(map_name: str) -> py.surface.Surface:
    try:
        return py.image.load(join(FLAG_PATH, map_name, "Map.png"))
    except FileNotFoundError:
        warn(f"Die Map für '{map_name}' konnte nicht gelanden werden!")
        return None

def load_category(category_path: str) -> dict[str, list[str]]:
    data = {}

    with open(join(CATEGORIES_PATH, category_path, "info.json"), "r", encoding="utf-8") as file:
        data = json.loads(file.read())

    return data

def load_flag_info(info_name: str) -> dict[str, list[str]]:
    data = {}

    try:
        with open(join(FLAG_PATH, info_name, "info.json"), "r", encoding="utf-8") as file:
            data = json.loads(file.read())
    except FileNotFoundError:
        warn(f"Die Info für '{info_name}' konnte nicht gelanden werden!")
        return None
    
    for k, v in data.items():
        data[k] = v.split("\n")
    
    return data

def center_x(width: int) -> int:
     return int((Config.get_window_width() - width) / 2)

def center_y(height: int) -> int:
     return int((Config.get_window_height() - height) / 2)

def wrapp_text(text: str, max_length: int) -> list[str]:
    value = [text]
    if len(text) > max_length:
        if text.find(" ") == -1: # if the text doesn't have a space then word wrapping doesn't make any sense
            return value

        last_space_index = text[:max_length].rfind(" ") # Get the index of the last space before the line end
        value = [text[:last_space_index], text[last_space_index + 1:]] # + 1 to not the the space at the start

    return value

def get_text_width(text: str, font: py.font.Font) -> int:
    return font.render(text, False, (0, 0, 0)).get_width()

if __name__ == "__main__":
    pass