from scr.utils import Utils

from scr.Flashcard import Flashcard

import threading as th

from os import listdir
from os.path import isdir, isfile, join

class Assets:
    COLLECTIONS: dict[str, list[str]]
    CATEGORIES: dict[str, list[str]]
    FLAGS: dict[str, Flashcard]
    FINISHED_LOADING = False

    @staticmethod
    def load_categories():
        Assets.COLLECTIONS = {}
        Assets.CATEGORIES = {}

        for collection in listdir(Utils.CATEGORIES_PATH): # For each file in /res/Collections
            if not isdir(join(Utils.CATEGORIES_PATH, collection)):
                continue
            Assets.COLLECTIONS[collection] = []

            for category in listdir(join(Utils.CATEGORIES_PATH, collection)): # For every Category in the collection
                if not isdir(join(Utils.CATEGORIES_PATH, collection, category)) or not isfile(join(Utils.CATEGORIES_PATH, collection, category, "Icon.png")): # only valid if a category has an icon image
                    continue
                Assets.COLLECTIONS[collection].append(category)

                Assets.CATEGORIES[category] = Utils.load_category(join(Utils.CATEGORIES_PATH, collection, category))

    @staticmethod
    def load_flags():
        Assets.FLAGS = {}

        load_at_a_time = 50 # how many flags are loaded in each thread
        flags = [f for f in listdir(Utils.FLAG_PATH)]
        flag_segments = []
        for i in range(0, len(flags), load_at_a_time): # Devide the flags in to chuncks
            flag_segments.append(flags[i:i + load_at_a_time])

        loaded_threads = []
        for s in flag_segments:
            loaded_threads.append(th.Thread(target=Assets._load_segement, args=(s,), daemon=True))

        for t in loaded_threads:
            t.start()

        for t in loaded_threads:
            t.join()

    @staticmethod
    def _load_segement(flags):
        for f in flags:
            Assets.FLAGS[f] = Flashcard(f)
