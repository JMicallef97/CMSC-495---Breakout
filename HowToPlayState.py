import arcade
import arcade.gui
from GameState import GameState
from GameView import GameView

# Represents the "How To Play" screen, displaying game instructions along with
# back and next navigation buttons.
class HowToPlayState(GameState):
    # Initialize the HowToPlayState instance.
    def __init__(self):
        super().__init__("How To Play")
        self.manager = arcade.gui.UIManager()  # Create UIManager for handling UI.
        self.manager.enable()

        # Create a back button to return to the main menu.
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Create a next button to proceed to the Game Start screen.
        self.next_button = arcade.gui.UIFlatButton(text="Next", width=100)
        self.next_button.on_click = self.on_click_next
        self.next_anchor = arcade.gui.UIAnchorLayout()
        self.next_anchor.add(anchor_x="right", anchor_y="top", child=self.next_button)
        self.manager.add(self.next_anchor)

        # Set the instructions text.
        instructions = (
            "How To Play:\n"
            "- Use arrow keys to move your paddle.\n"
            "- Bounce the ball to break bricks.\n"
            "- Don't let the ball fall!"
        )
        self.info_label = arcade.gui.UILabel(
            text=instructions,
            font_size=20,
            text_color=arcade.color.WHITE,
            multiline=True,
            width=400
        )
        # Center the instruction text.
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    # Handle the back button click event to return to the main menu.
    def on_click_back(self, event):
        self.manager.disable()
        import MainMenuState  # Local import to break circular dependency.
        arcade.get_window().show_view(GameView(StartMenuState.StartMenuState()))

    # Handle the next button click event to proceed to the Game Start screen.
    def on_click_next(self, event):
        self.manager.disable()
        import BreakoutGameState  # Local import.
        arcade.get_window().show_view(GameView(BreakoutGameState.GameStartState()))

    # Update the state (no periodic updates required).
    def updateState(self):
        pass

    # Draw the How To Play UI elements.
    def drawState(self):
        self.manager.draw()
