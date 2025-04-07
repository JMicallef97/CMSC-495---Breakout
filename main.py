import arcade

from Constants import Constants
from GameStateManager import GameStateManager
from InputManager import InputManager

# Static variables
# -Stores a reference to an instance of the GameData class, which is used to store
# game data that persists across multiple menus and settings.
#sessionData = GameData()

# -Game state manager (manages program/game flow and keeps track of the
# active game state)
gameStateMgr = GameStateManager()

# This class contains code used to manage user input, game logic and rendering,
# and the game window.
class GameView(arcade.View):

    # Constructor for the game class
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON

        # initialize the isKeyPressed dictionary with the keys used to control the game
        InputManager.isKeyPressed[arcade.key.A] = False   # used to move the paddle left during gameplay
        InputManager.isKeyPressed[arcade.key.D] = False   # used to move the paddle right during gameplay
        InputManager.isKeyPressed[arcade.key.P] = False   # used to pause the game.
        InputManager.isKeyPressed[arcade.key.Q] = False   # used to trigger quitting the game.

        # initialize the game state classes in the game state manager
        gameStateMgr.initGameStates()

        # set the starting game state here
        #gameStateMgr.setGameState("Test Menu")
        gameStateMgr.setGameState("Main Menu")

    # Contains code to update the game
    def on_update(self, delta_time):
        """All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that need it. """
        # Update the active game state
        gameStateMgr.updateActiveGameState()

    # Contains code to draw the game to the screen
    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        # Draw the active game state graphics
        gameStateMgr.drawActiveGameState()

    # Used to detect and handle key presses
    def on_key_press(self, key, key_modifiers):
        """ Called whenever a key on the keyboard is pressed.
        For a full list of keys, see: https://api.arcade.academy/en/latest/arcade.key.html """
        # check if the pressed key is contained within the isKeyPressed dictionary
        if key in InputManager.isKeyPressed:
            # change the state of the key to true (pressed)
            InputManager.isKeyPressed[key] = True


    # Used to detect and handle key releases
    def on_key_release(self, key, key_modifiers):
        """Called whenever the user lets off a previously pressed key."""
        # check if the released key is contained within the isKeyPressed dictionary
        if key in InputManager.isKeyPressed:
            # change the state of the key to false (released)
            InputManager.isKeyPressed[key] = False


    # Used to detect and handle mouse motion
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves."""
        # Update the moues X and Y coordinates
        InputManager.mouseCoordX = x
        InputManager.mouseCoordY = y



# Contains the entry point of the application/game, which is used to set up the game
# program
def main():

    """ Main function """

    #   Create a window class. This is what actually shows up on screen
    window = arcade.Window(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT, Constants.WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop (main game loop)
    arcade.run()

# Used to start the application
if __name__ == "__main__":

    main()