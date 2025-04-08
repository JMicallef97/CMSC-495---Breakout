import arcade

from Constants import Constants
from GameView import GameView
from InputManager import InputManager
from MainMenuState import MainMenuState

# This class contains code to set up and display the main menu program view, which is
# executed at program launch.
class ProgramView(arcade.View):

    # Instance variables
    # -Boolean, used to check if the main menu view has been initialized and displayed
    # or not.
    isMainMenuViewShown = False

    # -Stores a reference to a MainMenuState instance, which contains code to
    #  display and manage the main menu of the game (the starting state for the
    #  application).
    mainMenuState = None

    # Constructor for the game class
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON

        # initialize the isKeyPressed dictionary with the keys used to control the game
        InputManager.isKeyPressed[arcade.key.A] = False   # used to move the paddle left during gameplay
        InputManager.isKeyPressed[arcade.key.D] = False   # used to move the paddle right during gameplay
        InputManager.isKeyPressed[arcade.key.P] = False   # used to pause the game.
        InputManager.isKeyPressed[arcade.key.Q] = False   # used to trigger quitting the game.

    # Contains code to update the game
    def on_update(self, delta_time):
        """All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that need it. """
        # Check if the main menu has been shown yet
        if not self.isMainMenuViewShown:
            # create the main menu view, and switch to it
            self.mainMenuState = MainMenuState()
            arcade.get_window().show_view(GameView(self.mainMenuState))
            # update flag to avoid re-initializing the main menu state endlessly.
            self.isMainMenuViewShown = True

    # Contains code to draw the game to the screen
    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Check if the main menu view is initialized and ready to be shown
        if self.isMainMenuViewShown:
            # Draw the main menu state graphics
            self.mainMenuState.drawState()

# Contains the entry point of the application/game, which is used to set up the game
# program
def main():

    """ Main function """
    #   Create a window class. This is what actually shows up on screen
    window = arcade.Window(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT, Constants.WINDOW_TITLE)

    # Create and setup the starting game view
    game = ProgramView()

    # Show the game window to the screen
    window.show_view(game)

    # Start the arcade game loop (main game loop)
    arcade.run()

# Entry point for the program, used to start the application
if __name__ == "__main__":
    main()