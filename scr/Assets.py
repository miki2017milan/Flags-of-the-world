from scr.utils import Utils

from scr.Flashcard import Flashcard

import threading as th

from os import listdir
from os.path import isdir, isfile

class Assets:
    COLLECTIONS: dict[str, list[str]]
    CATEGORIES: dict[str, list[str]]
    FLAGS: dict[str, Flashcard]
    FINISHED_LOADING = False

    @staticmethod
    def load_categories():
        Assets.COLLECTIONS = {}
        Assets.CATEGORIES = {}
        for collection in listdir(Utils.CATEGORIES_PATH): # For each Collection from /res/Collections
            if isdir(Utils.CATEGORIES_PATH + collection):
                Assets.COLLECTIONS[collection] = []

                for f in listdir(Utils.CATEGORIES_PATH + collection): # For every Category the collection that has an icon image
                    if isdir(Utils.CATEGORIES_PATH + collection + "\\" + f) and isfile(Utils.CATEGORIES_PATH + collection + "\\" + f + "\\Icon.png"):
                        Assets.COLLECTIONS[collection].append(f)

                        Assets.CATEGORIES[f] = Utils.load_category(collection + "\\" + f)

    @staticmethod
    def load_flags():
        load_at_a_time = 50
        flags = [f.encode("utf-8").decode("utf-8") for f in listdir(Utils.FLAG_PATH)]
        flag_segments = []
        for i in range(0, len(flags), load_at_a_time):
            flag_segments.append(flags[i:i + load_at_a_time])

        load_threads = []
        Assets.FLAGS = {}
        for s in flag_segments:
            load_threads.append(th.Thread(target=Assets.load_segement, args=(s,)))

        for t in load_threads:
            t.start()

        for t in load_threads:
            t.join()

    def load_segement(flags):
        for f in flags:
            Assets.FLAGS[f] = Flashcard(f)
