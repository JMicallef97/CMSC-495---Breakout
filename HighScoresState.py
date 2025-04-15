import arcade
import arcade.gui
from GameState import GameState
from GameView import GameView

# Represents the High Scores state.
# Reads the top 10 scores from "highscores.txt" and displays them.
# If there are less than 10 scores, pads the remaining lines with "---".
# If the file does not exist, displays "No score file exists".
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
        file_exists = True
        try:
            with open("highscores.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    # Expected line format: "score - timestamp" (timestamp without seconds)
                    parts = line.split(" - ")
                    try:
                        score_val = int(parts[0])
                    except ValueError:
                        score_val = 0
                    scores_list.append((score_val, line))
        except FileNotFoundError:
            file_exists = False
        except Exception as e:
            print("Error reading high scores file:", e)
            file_exists = False

        # Build the display text depending on file existence.
        if not file_exists:
            scores_text = "No score file exists"
        else:
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
        # Disable the UI manager and return to the main menu.
        self.manager.disable()
        import MainMenuState  # Local import to break circular dependency.
        arcade.get_window().show_view(GameView(MainMenuState.MainMenuState()))

    def updateState(self):
        pass

    def drawState(self):
        self.manager.draw()
