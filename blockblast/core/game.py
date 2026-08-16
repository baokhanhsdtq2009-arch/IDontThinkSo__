import pygame

from core.state_manager import StateManager

from states.play_state import PlayState

from states.menu_state import MenuState


class Game:

    def __init__(
        self
    ):

        pygame.init()

        self.width = 1200

        self.height = 800

        self.screen = pygame.display.set_mode(

            (
                self.width,
                self.height
            )

        )

        pygame.display.set_caption(

            "Block Blast"

        )

        self.clock = pygame.time.Clock()

        self.running = True


        # STATE MANAGER

        self.state_manager = StateManager()


        # STATES

        self.state_manager.add_state(

            "menu",

            MenuState(
                self.state_manager
            )

        )

        self.state_manager.add_state(

            "play",

            PlayState(
                self.state_manager
            )

        )


        self.state_manager.set_state(

            "play"

        )


    def handle_events(
        self
    ):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False


            self.state_manager.handle_event(

                event

            )


    def update(
        self
    ):

        self.state_manager.update()


    def draw(
        self
    ):

        self.state_manager.draw(

            self.screen

        )

        pygame.display.flip()


    def run(
        self
    ):

        while self.running:

            self.clock.tick(

                60

            )

            self.handle_events()

            self.update()

            self.draw()


        pygame.quit()