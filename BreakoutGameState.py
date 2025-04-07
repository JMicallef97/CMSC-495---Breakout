import arcade
import arcade.gui

from Constants import Constants
from GameManager import GameManager
from GameState import GameState
from GameView import GameView
from InputManager import InputManager


# Represents the game start screen that displays a "Starting the game..." message.
# This screen will be replaced with the actual game.
class GameStartState(GameState):
    # Initialize the GameStartState instance.
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

