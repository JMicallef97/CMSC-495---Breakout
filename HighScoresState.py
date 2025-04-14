import arcade
import arcade.gui
from GameState import GameState
from GameView import GameView

# Represents the High Scores state.
# Reads the top 10 scores from "highscores.txt" and displays them.
# If there are less than 10 scores, it pads the list with "---".
class HighScoresState(GameState):
    def __init__(self):
        super().__init__("High Scores")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a Back button to return to the main menu.
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Read high scores from file "highscores.txt"
        scores_list = []
        try:
            with open("highscores.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    # Expected line format: "score - timestamp"
                    parts = line.split(" - ")
                    try:
                        score_val = int(parts[0])
                    except ValueError:
                        score_val = 0
                    scores_list.append((score_val, line))
        except Exception as e:
            print("Error reading high scores file:", e)

        # Sort scores descending (highest score first)
        scores_list.sort(key=lambda x: x[0], reverse=True)

        # Build a list of top 10 scores, padding with "---" if necessary.
        display_lines = []
        for idx in range(10):
            if idx < len(scores_list):
                display_lines.append(f"{idx+1}. {scores_list[idx][1]}")
            else:
                display_lines.append(f"{idx+1}. ---")
        scores_text = "\n".join(display_lines)

        # Create a label for displaying the scores.
        self.info_label = arcade.gui.UILabel(
            text=scores_text,
            font_size=20,
            text_color=arcade.color.WHITE,
            multiline=True,
            width=400
        )
        # Center the high scores label on the screen.
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        # Disable the current UI manager.
        self.manager.disable()
        # Local import to avoid circular dependencies.
        import MainMenuState
        # Transition to the main menu state.
        arcade.get_window().show_view(GameView(MainMenuState.MainMenuState()))

    def updateState(self):
        pass

    def drawState(self):
        self.manager.draw()
