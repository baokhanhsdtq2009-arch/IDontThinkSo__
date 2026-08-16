class StateManager:

    def __init__(self):

        self.states = {}

        self.current = None


    def add_state(
        self,
        name,
        state
    ):

        self.states[name] = state


    def set_state(
        self,
        name
    ):

        self.current = self.states[name]


    def update(self):

        if self.current:

            self.current.update()


    def draw(
        self,
        screen
    ):

        if self.current:

            self.current.draw(screen)


    def handle_event(
        self,
        event
    ):

        if self.current:

            self.current.handle_event(event)