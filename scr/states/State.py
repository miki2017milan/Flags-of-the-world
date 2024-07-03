from __future__ import annotations

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pygame as py
    from Main import Main

class State(ABC):
    state: State

    def __init__(self, main: Main):
        self.main = main

    @staticmethod
    def switch_state(state: State) -> None:
        State.state = state

    @staticmethod
    def get_state() -> State:
        return State.state

    @abstractmethod
    def tick(self) -> None:
        pass

    @abstractmethod
    def render(self, win: py.surface.Surface) -> None:
        pass