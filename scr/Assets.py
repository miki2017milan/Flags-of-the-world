import pygame as py
import scr.Utils as utils

from scr.Flashcard import Flashcard

from os import listdir
from os.path import isfile

class Assets:
    WINDOW_WIDTH: int = 1024
    WINDOW_HEIGHT: int = 1024

    GLOBE_IMG: py.surface.Surface
    NORTH_AMERICA_BUTTON: py.surface.Surface
    SOUTH_AMERICA_BUTTON: py.surface.Surface
    ASIA_BUTTON: py.surface.Surface
    EUROPE_BUTTON: py.surface.Surface
    AFRICA_BUTTON: py.surface.Surface
    OCEANIA_BUTTON: py.surface.Surface
    UN_BUTTON: py.surface.Surface

    CATEGORIES: dict[str, str]
    FLAGS: dict[str, Flashcard]
    
    @staticmethod
    def load_images():
        Assets.GLOBE_IMG = utils.load_image("Other_Images\\Globe.png")
        Assets.NORTH_AMERICA_BUTTON = utils.load_image("Other_Images\\NorthAmerica.png")
        Assets.SOUTH_AMERICA_BUTTON = utils.load_image("Other_Images\\SouthAmerica.png")
        Assets.ASIA_BUTTON = utils.load_image("Other_Images\\Asia.png")
        Assets.EUROPE_BUTTON = utils.load_image("Other_Images\\Europe.png")
        Assets.AFRICA_BUTTON = utils.load_image("Other_Images\\Africa.png")
        Assets.OCEANIA_BUTTON = utils.load_image("Other_Images\\Oceania.png")
        Assets.UN_BUTTON = utils.load_image("Other_Images\\UN.png")

    @staticmethod
    def load_categories():
        categories_file_names = [f.replace(".txt", "") for f in listdir(utils.CATEGORIES_PATH) if isfile(utils.CATEGORIES_PATH + f)]

        Assets.CATEGORIES = {}
        for c in categories_file_names:
            Assets.CATEGORIES[c] = utils.load_category(c)

    @staticmethod
    def load_flags():
        flags_files = [f.replace(".png", "") for f in listdir(utils.FLAG_PATH) if isfile(utils.FLAG_PATH + f)]
        flag_info_files = [f.replace(".json", "") for f in listdir(utils.FLAG_INFO_PATH) if isfile(utils.FLAG_INFO_PATH + f)]

        Assets.FLAGS = {}
        for f in flags_files:
            if f in flag_info_files:
                Assets.FLAGS[f] = Flashcard(f)
            else:
                print(f"LOAD ERROR: Flagge '{f}' konnte nicht geladen werden, da keine im Namen übereinstimmende Flaggen-Info-File existiert!")