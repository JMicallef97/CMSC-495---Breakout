import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"

# This class contains code used to manage user input, game logic and rendering,
# and the game window.
class GameView(arcade.View):

    # Constructor for the game class
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON

    # Resets the game to its initial state
    def reset(self):
        pass

    # Contains code to draw the game to the screen
    def on_draw(self):

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below


    # Contains code to update the game
    def on_update(self, delta_time):

        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        pass

    # Used to detect and handle key presses
    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass


    # Used to detect and handle key releases
    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass


    # Used to detect and handle mouse motion
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    # Used to detect and handle mouse clicks
    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    # Used to detect and handle releasing mouse buttons
    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass



# Contains the entry point of the application/game, which is used to set up the game
# program
def main():

    """ Main function """

    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop (main game loop)
    arcade.run()

# Used to start the application
if __name__ == "__main__":

    main()