import pygame as py
import scr.Utils as utils

from scr.Flashcard import Flashcard

from os import listdir
from os.path import isfile

class Assets:
    GLOBE_IMG: py.surface.Surface
    CATEGORIES: dict[str, str]
    FLAGS: dict[str, Flashcard]
    
    @staticmethod
    def load_images():
        Assets.GLOBE_IMG = utils.load_image("Other_Images\\Globe.png")

    @staticmethod
    def load_categories():
        categories_file_names = [f.replace(".txt", "") for f in listdir(utils.CATEGORIES_PATH) if isfile(utils.CATEGORIES_PATH + f)]

        Assets.CATEGORIES = {}
        for c in categories_file_names:
            Assets.CATEGORIES[c] = utils.load_category(c)

        print(Assets.CATEGORIES["Europe"])

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