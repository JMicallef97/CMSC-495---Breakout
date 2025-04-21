import arcade
import arcade.gui
from GameState import GameState
from GameView import GameView

# Represents the Game Over state.
# Displays a "Game Over" message along with the final score and three buttons:
# - Restart: Restart the game (transition to the Breakout game state).
# - Main Menu: Return to the main menu.
# - Exit Game: Close the application.
class GameOverState(GameState):
    def __init__(self, final_score):
        super().__init__("Game Over")
        self.final_score = final_score

        # Create and enable the UI manager for this state.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical box layout for the label and buttons.
        self.v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)

        # Create and add the Game Over label with the final score.
        game_over_label = arcade.gui.UILabel(
            text="Game Over!\nFinal Score: " + str(self.final_score),
            font_size=40,
            text_color=arcade.color.WHITE,
            multiline=True,
            width=400
        )
        self.v_box.add(game_over_label)
        self.v_box.add(arcade.gui.UISpace(height=20))

        # Create a Restart button to restart the game.
        restart_button = arcade.gui.UIFlatButton(text="Restart", width=200)
        restart_button.on_click = self.on_click_restart
        self.v_box.add(restart_button)

        # Create a Main Menu button to return to the main menu.
        menu_button = arcade.gui.UIFlatButton(text="Main Menu", width=200)
        menu_button.on_click = self.on_click_menu
        self.v_box.add(menu_button)

        # Create an Exit Game button to close the application.
        exit_button = arcade.gui.UIFlatButton(text="Exit Game", width=200)
        exit_button.on_click = self.on_click_exit
        self.v_box.add(exit_button)

        # Center the vertical layout on the screen.
        self.anchor = arcade.gui.UIAnchorLayout()
        self.anchor.add(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
        self.manager.add(self.anchor)

    def on_click_restart(self, event):
        # Disable the current UI manager.
        self.manager.disable()
        # Local import to avoid circular dependencies.
        import BreakoutGameState
        # Transition to the Breakout game state.
        arcade.get_window().show_view(GameView(BreakoutGameState.BreakoutGameState()))

    def on_click_menu(self, event):
        # Disable the current UI manager.
        self.manager.disable()
        # Local import to avoid circular dependencies.
        import MainMenuState
        # Transition to the main menu state.
        arcade.get_window().show_view(GameView(MainMenuState.MainMenuState()))

    def on_click_exit(self, event):
        # Disable the UI manager and close the window.
        self.manager.disable()
        arcade.close_window()

    def drawState(self):
        self.manager.draw()
