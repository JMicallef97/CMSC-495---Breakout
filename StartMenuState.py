import arcade
import arcade.gui
from GameView import GameView
from HowToPlayState import HowToPlayState
from AdjustDifficultyState import AdjustDifficultyState
from HighScoresState import HighScoresState
from GameState import GameState

# This class encapsulates the main menu UI and provides options for starting the game,
# adjusting difficulty, or viewing high scores.
class StartMenuState(GameState):
    # Initialize the StartMenuState instance.
    def __init__(self):
        super().__init__("Main Menu")
        self.manager = arcade.gui.UIManager()  # Create UIManager to handle UI elements.
        self.manager.enable()

        # Create a vertical layout for the menu items.
        self.v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)

        # Create and add the main title label.
        title_label = arcade.gui.UILabel(
            text="Main Screen", font_size=40, text_color=arcade.color.WHITE
        )
        self.v_box.add(title_label)
        self.v_box.add(arcade.gui.UISpace(height=50))  # Add spacing below the title.

        # Define the menu options.
        self.options = ["Start Game", "Adjust difficulty", "High Scores"]

        # Create a button for each menu option.
        for option in self.options:
            button = arcade.gui.UIFlatButton(text=option, width=200)
            self.v_box.add(button)
            button.on_click = self.make_option_click_handler(option)

        # Center the vertical layout on the screen.
        self.anchor = arcade.gui.UIAnchorLayout()
        self.anchor.add(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
        self.manager.add(self.anchor)

    # Create an event handler for menu button clicks.
    def make_option_click_handler(self, option):
        def on_click(event):
            self.manager.disable()  # Disable UI to avoid residual events.
            if option == "Start Game":
                view = GameView(HowToPlayState())
            elif option == "Adjust difficulty":
                view = GameView(AdjustDifficultyState())
            elif option == "High Scores":
                view = GameView(HighScoresState())
            arcade.get_window().show_view(view)
        return on_click

    # Update the state (no dynamic updates required in the main menu).
    def updateState(self):
        pass

    # Draw the main menu UI.
    def drawState(self):
        self.manager.draw()
