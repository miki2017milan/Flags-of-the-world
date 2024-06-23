import pygame as py
import json
import sys

RES_PATH = sys.path[0].replace("\\scr", "") + "\\res\\"
FLAG_INFO_PATH = RES_PATH + "Flags\\Flag_Info\\"
FLAG_PATH = RES_PATH + "Flags\\"
CATEGORIES_PATH = RES_PATH + "Categories\\"

def load_image(path: str):
    return py.image.load(RES_PATH + path)

def load_category(set_name: str) -> list[str]:
    data = []

    with open(CATEGORIES_PATH + set_name + ".txt", "r") as file:
        data = [line.rstrip() for line in file]

    return data

def load_flag_info(info_name: str) -> dict[str, str]:
        data = {}

        try:
            with open(FLAG_INFO_PATH + info_name + ".json", "r") as file:
                data = json.loads(file.read())
        except FileNotFoundError:
            raise FileNotFoundError(f"Datei '{FLAG_INFO_PATH + info_name + ".json"}' nicht gefunden!")
        
        return data

if __name__ == "__main__":
    pass