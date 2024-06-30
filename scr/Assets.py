from scr.utils import Utils

from scr.Flashcard import Flashcard

import threading as th

from os import listdir
from os.path import isfile

class Assets:
    CATEGORIES: dict[str, str]
    FLAGS: dict[str, Flashcard]
    FINISHED_LOADING = False

    @staticmethod
    def load_categories():
        categories_file_names = [f.replace(".txt", "") for f in listdir(Utils.CATEGORIES_PATH) if isfile(Utils.CATEGORIES_PATH + f)]

        Assets.CATEGORIES = {}
        for c in categories_file_names:
            Assets.CATEGORIES[c] = Utils.load_category(c)

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
