import pygame as py
import json
import sys

from scr.Button import Button

class Flashcard:
    def __init__(self, name: str, type_of_state: str):
        self.name = name

        res_path = sys.path[0] + "\\res\\"
        self.flag = py.image.load(res_path + f"{type_of_state}\\{name}.png")
        self.info = self.load_info(res_path + f"{type_of_state}\\Flag-Info\\{name}.json")

        # Center
        self.x = int((720 - self.flag.get_width()) / 2)
        self.y = int((500 - self.flag.get_height()) / 2)

        self.revealed = False
        self.reveal_button = Button(0, 500, 720, 524, "Reveal", (66, 66, 66), (66, 66, 66), (220, 220, 220), 120, 190, 190)

        self.name_font = py.font.SysFont("Calibri", 60, True)
        self.info_font = py.font.SysFont("Calibri", 40, False)
        self.text_color = (255, 255, 255)

    def load_info(self, info_path: str) -> dict[str, str]:
        data = {}

        try:
            with open(info_path) as file:
                data = json.loads(file.read())
        except FileNotFoundError:
            print(f"Datei '{info_path}' nicht gefunden!")
            exit()

        return data

    def render(self, win: py.surface.Surface) -> None:
        win.blit(self.flag, (self.x, self.y))

        if not self.revealed:
            self.reveal_button.render(win)
        else:
            py.draw.rect(win, (255, 255, 255), (0, 500, 720, 3))
            win.blit(self.name_font.render(self.name, False, (255, 255, 255)), (10, 530))

            # Draw added info from json file
            for i, (k, v) in enumerate(self.info.items()):
                win.blit(self.info_font.render(f"{k}: {v}", False, self.text_color), (10, 600 + i * 50))

        
