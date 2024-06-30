import threading as th
import time

from scr.Flashcard import Flashcard
from scr.utils import Utils
from os import listdir

FLAGS: dict
load_at_a_time = 50
def load_flags():
    flags = [f.encode("utf-8").decode("utf-8") for f in listdir(Utils.FLAG_PATH)]
    flag_segments = []
    for i in range(0, len(flags), load_at_a_time):
        flag_segments.append(flags[i:i + load_at_a_time])

    load_threads = []
    FLAGS = {}
    for s in flag_segments:
        load_threads.append(th.Thread(target=load_segement, args=(s,)))

    for t in load_threads:
        t.start()

    for t in load_threads:
        t.join()

def load_segement(flags):
    global FLAGS
    for f in flags:
        FLAGS[f] = Flashcard(f)

starttime = time.time()
load_flags()
endtime = time.time()
print(f"Startup Took: {endtime - starttime} s")