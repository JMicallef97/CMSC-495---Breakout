import arcade
import arcade.gui
from GameState import GameState


# ----------------------------
# Main Menu State and View
# ----------------------------
class StartMenuState(GameState):
    def __init__(self):
        super().__init__("Main Menu")
        # Set up the UI manager to hold our widgets
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical box layout for the title and buttons
        self.v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)

        # Title label at the top
        title_label = arcade.gui.UILabel(
            text="Main Screen", font_size=40, text_color=arcade.color.WHITE
        )
        self.v_box.add(title_label)
        # Add extra spacing after the title.
        self.v_box.add(arcade.gui.UISpace(height=50))

        # Define the menu options.
        self.options = ["Start Game", "How To Play", "Adjust difficulty", "High Scores"]

        # Create a button for each option.
        for option in self.options:
            button = arcade.gui.UIFlatButton(text=option, width=200)
            self.v_box.add(button)
            # Attach a click event that opens a different view based on the option.
            button.on_click = self.make_option_click_handler(option)

        # Center the layout in the window
        self.anchor = arcade.gui.UIAnchorLayout()
        self.anchor.add(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
        self.manager.add(self.anchor)

    def make_option_click_handler(self, option):
        # Returns a handler that opens a different view based on the option text
        def on_click(event):
            if option == "Start Game":
                view = StartGameStateView()
            elif option == "How To Play":
                view = HowToPlayStateView()
            elif option == "Adjust difficulty":
                view = AdjustDifficultyStateView()
            elif option == "High Scores":
                view = HighScoresStateView()
            arcade.get_window().show_view(view)

        return on_click

    def updateState(self):
        # No update logic required for the static main menu.
        pass

    def drawState(self):
        self.manager.draw()


class MainMenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = StartMenuState()

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_mouse_press(self, x, y, button, modifiers):
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.state.manager.on_mouse_release(x, y, button, modifiers)


# ----------------------------
# Start Game State and View
# ----------------------------
class StartGameState(GameState):
    def __init__(self):
        super().__init__("Start Game")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Back button at the top left
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Placeholder label to indicate the game is starting.
        self.info_label = arcade.gui.UILabel(
            text="Starting the game...", font_size=30, text_color=arcade.color.WHITE
        )
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        # Return to the main menu
        arcade.get_window().show_view(MainMenuView())

    def updateState(self):
        # Game-start logic would be added here.
        pass

    def drawState(self):
        self.manager.draw()


class StartGameStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = StartGameState()

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_mouse_press(self, x, y, button, modifiers):
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.state.manager.on_mouse_release(x, y, button, modifiers)


# ----------------------------
# How To Play State and View
# ----------------------------
class HowToPlayState(GameState):
    def __init__(self):
        super().__init__("How To Play")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Back button for returning to main menu.
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Instruction label with some sample text.
        instructions = (
            "How To Play:\n"
            "- Use arrow keys to move your paddle.\n"
            "- Bounce the ball to break bricks.\n"
            "- Don't let the ball fall!"
        )
        self.info_label = arcade.gui.UILabel(
            text=instructions, font_size=20, text_color=arcade.color.WHITE, multiline=True, width=400
        )
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        arcade.get_window().show_view(MainMenuView())

    def updateState(self):
        pass

    def drawState(self):
        self.manager.draw()


class HowToPlayStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = HowToPlayState()

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_mouse_press(self, x, y, button, modifiers):
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.state.manager.on_mouse_release(x, y, button, modifiers)


# ----------------------------
# Adjust Difficulty State and View
# ----------------------------
class AdjustDifficultyState(GameState):
    def __init__(self):
        super().__init__("Adjust Difficulty")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Back button at top left.
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Create a slider for difficulty adjustment.
        self.slider_label = arcade.gui.UILabel(
            text="Select Difficulty:", font_size=20, text_color=arcade.color.WHITE
        )
        self.difficulty_slider = arcade.gui.UISlider(value=50, width=300)

        # Box layout for slider and label.
        self.slider_box = arcade.gui.UIBoxLayout(vertical=True, space_between=10)
        self.slider_box.add(self.slider_label)
        self.slider_box.add(self.difficulty_slider)

        # Center the slider box.
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.slider_box)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        arcade.get_window().show_view(MainMenuView())

    def updateState(self):
        # You might add logic here to update difficulty based on slider value.
        pass

    def drawState(self):
        self.manager.draw()


class AdjustDifficultyStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = AdjustDifficultyState()

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_mouse_press(self, x, y, button, modifiers):
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.state.manager.on_mouse_release(x, y, button, modifiers)


# ----------------------------
# High Scores State and View
# ----------------------------
class HighScoresState(GameState):
    def __init__(self):
        super().__init__("High Scores")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Back button for returning to the main menu.
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Placeholder high scores display.
        scores = (
            "High Scores:\n"
             "1. AAA - 10000\n"
              "2. BBB - 8000\n"
            "    3. CCC - 6000"
        )
        self.info_label = arcade.gui.UILabel(
            text=scores, font_size=20, text_color=arcade.color.WHITE, multiline=True, width=400
        )
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        arcade.get_window().show_view(MainMenuView())

    def updateState(self):
        pass

    def drawState(self):
        self.manager.draw()


class HighScoresStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = HighScoresState()

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_mouse_press(self, x, y, button, modifiers):
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.state.manager.on_mouse_release(x, y, button, modifiers)
