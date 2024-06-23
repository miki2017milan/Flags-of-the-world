import pygame as py
import scr.Utils as utils

from scr.Button import Button

class Flashcard:
    def __init__(self, name: str):
        self.name = name

        self.flag = utils.load_image(f"Flags\\{name}.png")
        self.info = utils.load_flag_info(name)

        # Center
        self.x = int((720 - self.flag.get_width()) / 2)
        self.y = int((500 - self.flag.get_height()) / 2)

        self.revealed = False
        self.reveal_button = Button(0, 500, 720, 524, "Reveal", (66, 66, 66), (66, 66, 66), (220, 220, 220), 120, 190, 190)

        self.name_font = py.font.SysFont("Calibri", 60, True)
        self.info_font = py.font.SysFont("Calibri", 40, False)
        self.text_color = (255, 255, 255)

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

        
