import pygame

from core.base_state import BaseState
from gameplay.board import Board


class PlayState(BaseState):

    def __init__(
        self,
        state_manager
    ):

        self.state_manager = state_manager

        self.board = Board()


    def update(
        self
    ):

        self.board.update_hover(

            pygame.mouse.get_pos()

        )


    def draw(
        self,
        screen
    ):

        screen.fill(

            (0, 0, 0)

        )

        self.board.draw(

            screen

        )


    def handle_event(
        self,
        event
    ):

        pass