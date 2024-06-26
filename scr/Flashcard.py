import pygame as py

from scr.utils import Utils, Config

class Flashcard:
    def __init__(self, name: str):
        self.info = Utils.load_flag_info(name)
        for k, v in self.info.items():
            self.info[k] = v.split("\n")

        self.flag = Utils.load_flag(name)
        self.flag_x = Utils.center_x(self.flag.get_width())
        self.flag_y = 50

        self.map = Utils.load_map(name)
        if self.map:
            self.map_x = Utils.center_x(self.map.get_width())
            self.map_y = Utils.center_y(self.map.get_height()) + 50

        self.LINE_HEIGHT = 50
        self.mode = 0

        self.name_font = py.font.SysFont("Calibri", 60, True)
        self.info_font = py.font.SysFont("Calibri", 40, False)
        self.reveal_font = py.font.SysFont("Calibri", 80, False)
        self.text_color = (255, 255, 255)

        self.name = [name]
        self.name_pos = [Utils.center_x(self.get_text_width(self.name[0]))]

        # Split the name if its to long to make it look better
        if len(name) > 25:
            temp = name[:25].rfind(" ") # Get the index of the last space before the line end
            self.name = [name[:temp], name[temp + 1:]] # + 1 to not the the space at the start

            self.name_pos = [Utils.center_x(self.get_text_width(self.name[0])), Utils.center_x(self.get_text_width(self.name[1]))]

    def get_text_width(self, text: str) -> int:
        return self.name_font.render(text, False, (0, 0, 0)).get_width()

    def render_map(self, win: py.surface.Surface) -> None:
        if self.map:
            win.blit(self.map, (self.map_x, self.map_y))
            # Draw name
            for i, j in enumerate(self.name):
                win.blit(self.name_font.render(j, False, (255, 255, 255)), (self.name_pos[i], 10 + i * self.LINE_HEIGHT))
        else:
            win.blit(self.name_font.render("No map available", False, (255, 255, 255)), (300, 480))

    def render_info(self, win: py.surface.Surface) -> None:
        line_num = 0 # Track the current line

        # Draw name
        for i, j in enumerate(self.name):
            win.blit(self.name_font.render(j, False, (255, 255, 255)), (self.name_pos[i], 500 + line_num * self.LINE_HEIGHT))
            line_num += 1

        # Draw deviding line
        py.draw.rect(win, (255, 255, 255), (0, 500 + line_num * (self.LINE_HEIGHT + 10), Config.get_window_width(), 3))

        # Draw added info from json file
        for k, v in self.info.items():
            win.blit(self.info_font.render(f"{k}: {v[0]}", False, self.text_color), (10, 540 + line_num * self.LINE_HEIGHT))
            line_num += 1

            # If the value is multilined
            for t in v[1:]:
                win.blit(self.info_font.render(f"{t}", False, self.text_color), (10, 540 + line_num * self.LINE_HEIGHT))
                line_num += 1

    def render(self, win: py.surface.Surface) -> None:
        if self.mode == 0:
            win.blit(self.flag, (self.flag_x, self.flag_y))
            py.draw.rect(win, (100, 100, 100), (0, 500, Config.get_window_width(), Config.get_window_height()))
        elif self.mode == 1:
            win.blit(self.flag, (self.flag_x, self.flag_y))
            self.render_info(win)
        else:
            self.render_map(win)

    def next_mode(self) -> None:
        self.mode += 1

    def get_mode(self) -> int:
        return self.mode
    
    def reset_mode(self) -> None:
        self.mode = 0
