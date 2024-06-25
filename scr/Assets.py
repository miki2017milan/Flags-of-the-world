from scr.utils import Utils

from scr.Flashcard import Flashcard

from os import listdir
from os.path import isfile

class Assets:
    CATEGORIES: dict[str, str]
    FLAGS: dict[str, Flashcard]

    @staticmethod
    def load_categories():
        categories_file_names = [f.replace(".txt", "") for f in listdir(Utils.CATEGORIES_PATH) if isfile(Utils.CATEGORIES_PATH + f)]

        Assets.CATEGORIES = {}
        for c in categories_file_names:
            Assets.CATEGORIES[c] = Utils.load_category(c)

    @staticmethod
    def load_flags():
        flags = [f.encode("utf-8").decode("utf-8") for f in listdir(Utils.FLAG_PATH)]

        Assets.FLAGS = {}
        for f in flags:
            if isfile(Utils.FLAG_PATH + f + "\\" + f + ".json"):
                Assets.FLAGS[f] = Flashcard(f)
            else:
                pass
                # print(f"LOAD ERROR: Flagge '{f}' konnte nicht geladen werden, da keine im Namen übereinstimmende Flaggen-Info-File existiert!")