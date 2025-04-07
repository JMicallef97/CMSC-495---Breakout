import arcade
import arcade.gui
from GameState import GameState
from GameView import GameView

# Provides the UI for displaying high scores with a back button to return to the main menu.
class HighScoresState(GameState):
    # Initialize the HighScoresState instance.
    def __init__(self):
        super().__init__("High Scores")
        self.manager = arcade.gui.UIManager()  # Create UIManager.
        self.manager.enable()

        # Create a back button to return to the main menu.
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Define high scores display text.
        # This will be replaced with the code to import file containing the scores.
        scores = (
            "High Scores:\n"
            "1. AAA - 10000\n"
            "2. BBB - 8000\n"
            "3. CCC - 6000\n"
            "4. ----\n"
            "5. ----\n"
            "6. ----\n"
            "7. ----\n"
            "8. ----\n"
            "9. ----\n"
            "10. ----\n"


        )
        self.info_label = arcade.gui.UILabel(
            text=scores,
            font_size=20,
            text_color=arcade.color.WHITE,
            multiline=True,
            width=400
        )
        # Center the high scores text.
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    # Handle the back button click event to return to the main menu.
    def on_click_back(self, event):
        self.manager.disable()
        import MainMenuState
        arcade.get_window().show_view(GameView(MainMenuState.MainMenuState()))

    # Update the state (no dynamic updates needed).
    def updateState(self):
        pass

    # Draw the High Scores UI.
    def drawState(self):
        self.manager.draw()
