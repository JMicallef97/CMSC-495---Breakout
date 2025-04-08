import arcade
import arcade.gui

from GameView import GameView
from HowToPlayState import HowToPlayState
from AdjustDifficultyState import AdjustDifficultyState
from HighScoresState import HighScoresState
from GameState import GameState

# This class encapsulates code to set up and display the difficulty adjustment menu,
# providing event handlers for the menu controls (buttons to start the game, access the
# game difficulty adjustment menu, or access the high scores menu).
class MainMenuState(GameState):
    def __init__(self):
        # Initialize the base GameState with the name "Main Menu"
        super().__init__("Main Menu")
        # Create and enable a UI manager to manage all UI widgets
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical layout to hold the title and buttons
        self.v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)

        # Create the title label for the main menu
        title_label = arcade.gui.UILabel(
            text="Main Screen", font_size=40, text_color=arcade.color.WHITE
        )
        self.v_box.add(title_label)
        # Add extra vertical space after the title
        self.v_box.add(arcade.gui.UISpace(height=50))

        # Define the three main menu options
        self.options = ["Start Game", "Adjust difficulty", "High Scores"]

        # Create a button for each option and attach an event handler
        for option in self.options:
            button = arcade.gui.UIFlatButton(text=option, width=200)
            self.v_box.add(button)
            button.on_click = self.make_option_click_handler(option)

        # Center the layout on the screen
        self.anchor = arcade.gui.UIAnchorLayout()
        self.anchor.add(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
        self.manager.add(self.anchor)

    def make_option_click_handler(self, option):
        """
        Returns a click event handler that switches to the appropriate state.
        """
        def on_click(event):
            # Disable the current UI manager to prevent further interactions
            self.manager.disable()
            # Choose the new state based on the option clicked
            if option == "Start Game":
                view = GameView(HowToPlayState())
            elif option == "Adjust difficulty":
                view = GameView(AdjustDifficultyState())
            elif option == "High Scores":
                view = GameView(HighScoresState())
            # Switch to the new view
            arcade.get_window().show_view(view)
        return on_click

    def updateState(self):
        # Main menu is static; no dynamic update required.
        pass

    def drawState(self):
        # Draw the UI for the main menu
        self.manager.draw()
