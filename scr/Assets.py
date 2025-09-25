from scr.utils import Utils

from scr.Flashcard import Flashcard

import threading as th

from os import listdir
from os.path import isdir, isfile, join
from itertools import batched

class Assets:
    COLLECTIONS: dict[str, list[str]] # Group of categories e.g (Nations: [Europe, North America, ...], Dependent terretories: [...])
    CATEGORIES: dict[str, dict[str, list[str] | str]] # Group of flags e.g (Europe: {Countries: [...], Description: "..."}, North America: ...)
    FLAGS: dict[str, Flashcard] # All Flags
    FINISHED_LOADING = False

    @staticmethod
    def load_categories():
        Assets.COLLECTIONS = {}
        Assets.CATEGORIES = {}

        for collection in listdir(Utils.COLLECTIONS_PATH): # For each element in /res/Collections
            if not isdir(join(Utils.COLLECTIONS_PATH, collection)):
                continue
            Assets.COLLECTIONS[collection] = []

            for category in listdir(join(Utils.COLLECTIONS_PATH, collection)): # For every element in the collection
                if not isdir(join(Utils.COLLECTIONS_PATH, collection, category)) or not isfile(join(Utils.COLLECTIONS_PATH, collection, category, "Icon.png")): # only valid if a category has an icon image
                    continue
                Assets.COLLECTIONS[collection].append(category)

                Assets.CATEGORIES[category] = Utils.load_category_info(collection, category)

    @staticmethod
    def load_flags():
        Assets.FLAGS = {}

        LOAD_AT_A_TIME = 10 # how many flags are loaded in each thread
        flags = [f for f in listdir(Utils.FLAG_PATH)]
        flag_segments = batched(flags, n=LOAD_AT_A_TIME)

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
