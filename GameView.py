import arcade

from InputManager import InputManager


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

    # Used to detect and handle key presses. Key presses should be processed within the
    # self.state's updateState function.
    def on_key_press(self, key, key_modifiers):
        """ Called whenever a key on the keyboard is pressed.
        For a full list of keys, see: https://api.arcade.academy/en/latest/arcade.key.html """
        # check if the pressed key is contained within the isKeyPressed dictionary
        if key in InputManager.isKeyPressed:
            # change the state of the key to true (pressed)
            InputManager.isKeyPressed[key] = True

    # Used to detect and handle key presses. Key presses should be processed within the
    # self.state's updateState function.
    def on_key_release(self, key, key_modifiers):
        """ Called whenever a key on the keyboard is pressed.
        For a full list of keys, see: https://api.arcade.academy/en/latest/arcade.key.html """
        # check if the released key is contained within the isKeyPressed dictionary
        if key in InputManager.isKeyPressed:
            # change the state of the key to true (pressed)
            InputManager.isKeyPressed[key] = False

    # Runs the code to handle mouse clicks within the view.
    def on_mouse_press(self, x, y, button, modifiers):
        """Called when the user presses a mouse button."""
        # Check if the left mouse button was pressed
        if button is arcade.MOUSE_BUTTON_LEFT:
            # change the state of isLeftMouseButtonPressed to true (pressed)
            InputManager.isLeftMouseButtonPressed = True
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    # Used to detect and handle releasing the left mouse button.
    def on_mouse_release(self, x, y, button, key_modifiers):
        """Called when a user releases a mouse button."""
        # Check if the left mouse button was released
        if button == arcade.MOUSE_BUTTON_LEFT:
            # change the state of isLeftMouseButtonReleased to true (pressed)
            InputManager.isLeftMouseButtonPressed = False

    # Used to detect and handle mouse motion
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves."""
        # Update the moues X and Y coordinates
        InputManager.mouseCoordX = x
        InputManager.mouseCoordY = y

    # Runs the code to disable interaction with this game view when the view is
    # hidden [back button pressed] to avoid buggy behavior.
    def on_hide_view(self):
        self.state.manager.disable()