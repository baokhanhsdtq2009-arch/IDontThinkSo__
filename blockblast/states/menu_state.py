from core.base_state import BaseState


class MenuState(BaseState):

    def __init__(
        self,
        state_manager
    ):

        self.state_manager = state_manager


    def update(
        self
    ):

        pass


    def draw(
        self,
        screen
    ):

        screen.fill(
            (40,40,40)
        )


    def handle_event(
        self,
        event
    ):

        pass