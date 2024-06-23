import pygame as py
import scr.Utils as utils

class Flashcard:
    def __init__(self, name: str):
        self.info = utils.load_flag_info(name)
        for k, v in self.info.items():
            self.info[k] = v.split("\n")

        self.flag = utils.load_image(f"Flags\\{name}.png")
        self.flag_x = utils.center_x(self.flag.get_width())
        self.flag_y = 50

        self.LINE_HEIGHT = 50
        self.revealed = False
        self.map_mode = False

        self.name_font = py.font.SysFont("Calibri", 60, True)
        self.info_font = py.font.SysFont("Calibri", 40, False)
        self.reveal_font = py.font.SysFont("Calibri", 80, False)
        self.text_color = (255, 255, 255)

        self.name = [name]
        self.name_pos = [utils.center_x(self.get_text_width(self.name[0]))]

        # Split the name if its to long to make it look better
        if len(name) > 25:
            temp = name[:25].rfind(" ") # Get the index of the last space before the line end
            self.name = [name[:temp], name[temp + 1:]] # + 1 to not the the space at the start

            self.name_pos = [utils.center_x(self.get_text_width(self.name[0])), utils.center_x(self.get_text_width(self.name[1]))]

    def get_text_width(self, text: str) -> int:
        return self.name_font.render(text, False, (0, 0, 0)).get_width()

    def render_map(self, win: py.surface.Surface) -> None:
        pass

    def render_info(self, win: py.surface.Surface) -> None:
        line_num = 0 # Track the current line

        # Draw name
        for i, j in enumerate(self.name):
            win.blit(self.name_font.render(j, False, (255, 255, 255)), (self.name_pos[i], 500 + line_num * self.LINE_HEIGHT))
            line_num += 1

        # Draw deviding line
        py.draw.rect(win, (255, 255, 255), (0, 500 + line_num * (self.LINE_HEIGHT + 10), 1024, 3))

        # Draw added info from json file
        for k, v in self.info.items():
            win.blit(self.info_font.render(f"{k}: {v[0]}", False, self.text_color), (10, 540 + line_num * self.LINE_HEIGHT))
            line_num += 1

            # If the value is multilined
            for t in v[1:]:
                win.blit(self.info_font.render(f"{t}", False, self.text_color), (10, 540 + line_num * self.LINE_HEIGHT))
                line_num += 1

    def render(self, win: py.surface.Surface) -> None:
        win.blit(self.flag, (self.flag_x, self.flag_y))

        if self.revealed:
            if not self.map_mode:
                self.render_info(win)
                return
            self.render_map(win)

        py.draw.rect(win, (100, 100, 100), (0, 500, 1024, 524))

        
