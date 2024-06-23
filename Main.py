import pygame as py

from scr.states.GameState import GameState
from scr.states.MenuState import MenuState
from scr.states.State import State
from scr.Assets import Assets

py.init()

class Main:
    def __init__(self):
        # Window
        self.WIDTH = 720
        self.HEIGHT = 1024

        self.win = py.display.set_mode((self.WIDTH, self.HEIGHT))
        py.display.set_caption("Flags of the World")

        # Tick
        self.clock = py.time.Clock()
        self.FPS = 60
        self.running = True

        Assets.load_images()
        Assets.load_categories()
        Assets.load_flags()

        # States
        self.menu_state = MenuState(self)
        self.game_state = GameState(self)

        State.switch_state(self.menu_state)

    def tick(self) -> None:
        for e in py.event.get():
            if e.type == py.QUIT:
                self.running = False
            if e.type == py.KEYDOWN:
                if e.key == py.K_ESCAPE:
                    self.running = False

        State.get_state().tick()

        self.clock.tick(self.FPS)

    def render(self) -> None:
        # Background in case the State has no background
        self.win.fill((200, 0, 200))
            
        State.get_state().render(self.win)
        
        py.display.update()

    def run(self) -> None:
        while self.running:
            self.render()
            self.tick()

        py.quit()
        exit()

if __name__ == "__main__":
    main = Main()
    main.run()