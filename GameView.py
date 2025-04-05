import arcade

# This class is used as a starting point for the different game view objects,
# encapsulating functions often used in game view states to avoid code duplication.
# NOTE: Classes that inherit from this class must initialize self.state in the
# constructor in order for the code to work properly.
class GameView(arcade.View):

    # Constructor for the GameView object.
    def __init__(self, viewState):
        super().__init__()
        self.state = viewState # Will be populated by child classes.

    # Draws the game state graphics to the screen.
    def on_draw(self):
        self.clear()
        self.state.drawState()

    # Runs the code to update the game state.
    def on_update(self, delta_time):
        self.state.updateState()

    # Runs the code to handle mouse clicks within the view.
    def on_mouse_press(self, x, y, button, modifiers):
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    # Key presses should be handled within self.state's updateState() function.

    # Runs the code to disable interaction with this game view when the view is
    # hidden [back button pressed] to avoid buggy behavior.
    def on_hide_view(self):
        self.state.manager.disable()