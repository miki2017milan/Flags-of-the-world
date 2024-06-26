import pygame as py
import json
import sys

from scr.utils import Config

RES_PATH = sys.path[0].replace("\\scr", "") + "\\res\\"
FLAG_PATH = RES_PATH + "Flags\\"
CATEGORIES_PATH = RES_PATH + "Collections\\"

def load_image(image_name: str) :
    return py.image.load(RES_PATH + image_name + ".png")

def load_flag(flag_name: str):
    return py.image.load(FLAG_PATH + f"{flag_name}\\{flag_name}.png")

def load_map(map_name: str) :
    try:
        return py.image.load(FLAG_PATH + f"{map_name}\\Map.png")
    except FileNotFoundError:
        # print(f"MAP ERROR: Die Map '{FLAG_PATH + f"{map_name}\\{map_name}_Map.png"}' konnte nicht gelanden werden!")
        return

def load_category(category_path: str) -> dict[str, list | str]:
    data = {}

    with open(CATEGORIES_PATH + category_path + "\\info.json", "r", encoding="utf-8") as file:
        data = json.loads(file.read())

    return data

def load_flag_info(info_name: str) -> dict[str, str]:
        data = {}

        try:
            with open(FLAG_PATH + f"{info_name}\\{info_name}.json", "r", encoding="utf-8") as file:
                data = json.loads(file.read())
        except FileNotFoundError:
            return
        
        for k, v in data.items():
            data[k] = v.split("\n")
        
        return data

def center_x(width: int) -> int:
     return int((Config.get_window_width() - width) / 2)

def center_y(height: int) -> int:
     return int((Config.get_window_height() - height) / 2)

if __name__ == "__main__":
    pass