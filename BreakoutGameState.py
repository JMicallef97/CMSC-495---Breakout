import arcade
import arcade.gui
from Constants import Constants
from GameManager import GameManager
from GameState import GameState

# This class encapsulates code to set up and display the Breakout gameplay game state,
# providing methods to update and draw the state (handled by an instance of the GameManager
# class).
class BreakoutGameState(GameState):
    # Initialize the BreakoutGameState instance.
    def __init__(self):
        super().__init__("Breakout Game State")
        self.game_manager = GameManager(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)

        self.manager = arcade.gui.UIManager()  # Create UIManager.
        self.manager.enable()

    # Update the Breakout game code.
    def updateState(self):
        self.game_manager.update()

    # Draw the Breakout game graphics (ball, brick, paddle, etc)
    def drawState(self):
        self.game_manager.draw()
        self.manager.draw()

