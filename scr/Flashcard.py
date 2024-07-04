import pygame as py
py.init()

from scr.utils import Utils, Config

class Flashcard:
    def __init__(self, name: str):
        self.info = Utils.load_flag_info(name)

        self.flag = Utils.load_flag(name)
        self.flag_x = Utils.center_x(self.flag.get_width())
        self.flag_y = 50

        self.map = Utils.load_map(name)
        if self.map:
            self.map_x = Utils.center_x(self.map.get_width())
            self.map_y = Utils.center_y(self.map.get_height()) + 70

        self.LINE_HEIGHT = 50 # For rendering the information
        self.mode = 0 # 0 = Draw Flag unreveald, 1 = reveald info, 2 = show map

        self.name_font = py.font.SysFont("Calibri", 60, True)
        self.info_font = py.font.SysFont("Calibri", 40, False)
        self.text_color = (255, 255, 255)

        self.name_pos = []
        self.name = Utils.wrapp_text(name, 25)
        for part in self.name:
            self.name_pos.append(Utils.center_x(Utils.get_text_width(part, self.name_font)))

    def render_map(self, win: py.surface.Surface) -> None:
        if self.map:
            win.blit(self.map, (self.map_x, self.map_y))
            # Draw name
            for i, name_part in enumerate(self.name):
                win.blit(self.name_font.render(name_part, False, self.text_color), (self.name_pos[i], 10 + i * self.LINE_HEIGHT))
            return
        
        win.blit(self.name_font.render("No map available", False, (255, 255, 255)), (Utils.center_x(self.get_text_width("No map available")), 500))

    def render_info(self, win: py.surface.Surface) -> None:
        line_num = 0 # Track the current line

        # Draw name
        for i, name_part in enumerate(self.name):
            win.blit(self.name_font.render(name_part, False, (255, 255, 255)), (self.name_pos[i], 500 + line_num * self.LINE_HEIGHT))
            line_num += 1

        # Draw deviding line
        py.draw.rect(win, (255, 255, 255), (0, 500 + line_num * (self.LINE_HEIGHT + 10), Config.get_window_width(), 3))

        if not self.info:
            return

        # Draw info from json file
        for k, v in self.info.items():
            win.blit(self.info_font.render(f"{k}: {v[0]}", False, self.text_color), (10, 540 + line_num * self.LINE_HEIGHT))
            line_num += 1

            # If the info is multilined
            for line in v[1:]:
                win.blit(self.info_font.render(f"{line}", False, self.text_color), (10, 540 + line_num * self.LINE_HEIGHT))
                line_num += 1

    def render(self, win: py.surface.Surface) -> None:
        if self.mode == 0: # unreveald flag
            win.blit(self.flag, (self.flag_x, self.flag_y))
            py.draw.rect(win, (100, 100, 100), (0, 500, Config.get_window_width(), Config.get_window_height()))
        elif self.mode == 1: # reveald
            win.blit(self.flag, (self.flag_x, self.flag_y))
            self.render_info(win)
        else: # map
            self.render_map(win)
