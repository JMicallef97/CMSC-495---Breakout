import arcade
import arcade.gui

from Constants import Constants
from GameManager import GameManager
from GameState import GameState
from GameView import GameView

# Represents the game start screen that displays a "Starting the game..." message.
# This screen will be replaced with the actual game.
class GameStartState(GameState):
    # Initialize the GameStartState instance.
    def __init__(self):
        super().__init__("Game Start")
        self.game_manager = GameManager(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)

        self.manager = arcade.gui.UIManager()  # Create UIManager.
        self.manager.enable()

        # Create a back button to return to the How To Play screen.
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Display the "Starting the game..." message.
        self.info_label = arcade.gui.UILabel(
            text="Starting the game...", font_size=30, text_color=arcade.color.WHITE
        )
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    # Handle the back button click event to return to the How To Play screen.
    def on_click_back(self, event):
        self.manager.disable()
        import HowToPlayState  # Local import.
        arcade.get_window().show_view(GameView(HowToPlayState.HowToPlayState()))

    # Update the state (no dynamic updates needed).
    def updateState(self):
        self.game_manager.update()
        pass

    # Draw the Game Start UI.
    def drawState(self):
        self.game_manager.draw()
        self.manager.draw()

