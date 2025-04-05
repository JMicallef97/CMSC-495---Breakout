import arcade
import arcade.gui
from arcade.gui.widgets.slider import UISlider
from arcade.gui.events import UIOnChangeEvent
from GameState import GameState

# ----------------------------
# Main Menu State and View
# ----------------------------
class StartMenuState(GameState):
    def __init__(self):
        super().__init__("Main Menu")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)

        title_label = arcade.gui.UILabel(
            text="Main Screen", font_size=40, text_color=arcade.color.WHITE
        )
        self.v_box.add(title_label)
        self.v_box.add(arcade.gui.UISpace(height=50))

        # Options: Start Game, Adjust difficulty, High Scores
        self.options = ["Start Game", "Adjust difficulty", "High Scores"]

        for option in self.options:
            button = arcade.gui.UIFlatButton(text=option, width=200)
            self.v_box.add(button)
            button.on_click = self.make_option_click_handler(option)

        self.anchor = arcade.gui.UIAnchorLayout()
        self.anchor.add(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
        self.manager.add(self.anchor)

    def make_option_click_handler(self, option):
        def on_click(event):
            self.manager.disable()
            if option == "Start Game":
                view = PreGameStateView()
            elif option == "Adjust difficulty":
                view = AdjustDifficultyStateView()
            elif option == "High Scores":
                view = HighScoresStateView()
            arcade.get_window().show_view(view)
        return on_click

    def updateState(self):
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

    def on_hide_view(self):
        self.state.manager.disable()


# ----------------------------
# Pre-Game State (How-To-Play Instructions) and View
# ----------------------------
class PreGameState(GameState):
    def __init__(self):
        super().__init__("Pre Game")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        self.next_button = arcade.gui.UIFlatButton(text="Next", width=100)
        self.next_button.on_click = self.on_click_next
        self.next_anchor = arcade.gui.UIAnchorLayout()
        self.next_anchor.add(anchor_x="right", anchor_y="top", child=self.next_button)
        self.manager.add(self.next_anchor)

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
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        self.manager.disable()
        arcade.get_window().show_view(MainMenuView())

    def on_click_next(self, event):
        self.manager.disable()
        arcade.get_window().show_view(GameStartStateView())

    def updateState(self):
        pass

    def drawState(self):
        self.manager.draw()


class PreGameStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = PreGameState()

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_mouse_press(self, x, y, button, modifiers):
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.state.manager.on_mouse_release(x, y, button, modifiers)

    def on_hide_view(self):
        self.state.manager.disable()


# ----------------------------
# Game Start State and View (Actual Start Game Page)
# ----------------------------
class GameStartState(GameState):
    def __init__(self):
        super().__init__("Game Start")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        self.info_label = arcade.gui.UILabel(
            text="Starting the game...", font_size=30, text_color=arcade.color.WHITE
        )
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        self.manager.disable()
        arcade.get_window().show_view(PreGameStateView())

    def updateState(self):
        pass

    def drawState(self):
        self.manager.draw()


class GameStartStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = GameStartState()

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_mouse_press(self, x, y, button, modifiers):
        self.state.manager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.state.manager.on_mouse_release(x, y, button, modifiers)

    def on_hide_view(self):
        self.state.manager.disable()


# ----------------------------
# Adjust Difficulty State and View (Using UISlider)
# ----------------------------
class AdjustDifficultyState(GameState):
    def __init__(self):
        super().__init__("Adjust Difficulty")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        # Vertical layout to hold the slider groups.
        self.slider_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)

        # --- Paddle Width Slider ---
        paddle_width_desc = arcade.gui.UILabel(
            text="Adjust paddle width:", font_size=20, text_color=arcade.color.WHITE
        )
        self.paddle_width_slider = UISlider(value=5, width=300, height=50, min_value=1, max_value=10, step=1)
        paddle_width_value_label = arcade.gui.UILabel(
            text=f"{int(self.paddle_width_slider.value)}", font_size=16, text_color=arcade.color.WHITE
        )
        @self.paddle_width_slider.event("on_change")
        def on_change_pw(event: UIOnChangeEvent):
            paddle_width_value_label.text = f"{int(self.paddle_width_slider.value)}"
            paddle_width_value_label.fit_content()
        paddle_width_hbox = arcade.gui.UIBoxLayout(vertical=False, space_between=10)
        paddle_width_hbox.add(self.paddle_width_slider)
        paddle_width_hbox.add(paddle_width_value_label)
        paddle_width_box = arcade.gui.UIBoxLayout(vertical=True, space_between=5)
        paddle_width_box.add(paddle_width_desc)
        paddle_width_box.add(paddle_width_hbox)
        self.slider_box.add(paddle_width_box)

        # --- Paddle Movement Speed Slider ---
        paddle_speed_desc = arcade.gui.UILabel(
            text="Adjust paddle movement speed:", font_size=20, text_color=arcade.color.WHITE
        )
        self.paddle_speed_slider = UISlider(value=5, width=300, height=50, min_value=1, max_value=10, step=1)
        paddle_speed_value_label = arcade.gui.UILabel(
            text=f"{int(self.paddle_speed_slider.value)}", font_size=16, text_color=arcade.color.WHITE
        )
        @self.paddle_speed_slider.event("on_change")
        def on_change_ps(event: UIOnChangeEvent):
            paddle_speed_value_label.text = f"{int(self.paddle_speed_slider.value)}"
            paddle_speed_value_label.fit_content()
        paddle_speed_hbox = arcade.gui.UIBoxLayout(vertical=False, space_between=10)
        paddle_speed_hbox.add(self.paddle_speed_slider)
        paddle_speed_hbox.add(paddle_speed_value_label)
        paddle_speed_box = arcade.gui.UIBoxLayout(vertical=True, space_between=5)
        paddle_speed_box.add(paddle_speed_desc)
        paddle_speed_box.add(paddle_speed_hbox)
        self.slider_box.add(paddle_speed_box)

        # --- Ball Movement Speed Slider ---
        ball_speed_desc = arcade.gui.UILabel(
            text="Adjust ball movement speed:", font_size=20, text_color=arcade.color.WHITE
        )
        self.ball_speed_slider = UISlider(value=5, width=300, height=50, min_value=1, max_value=10, step=1)
        ball_speed_value_label = arcade.gui.UILabel(
            text=f"{int(self.ball_speed_slider.value)}", font_size=16, text_color=arcade.color.WHITE
        )
        @self.ball_speed_slider.event("on_change")
        def on_change_bs(event: UIOnChangeEvent):
            ball_speed_value_label.text = f"{int(self.ball_speed_slider.value)}"
            ball_speed_value_label.fit_content()
        ball_speed_hbox = arcade.gui.UIBoxLayout(vertical=False, space_between=10)
        ball_speed_hbox.add(self.ball_speed_slider)
        ball_speed_hbox.add(ball_speed_value_label)
        ball_speed_box = arcade.gui.UIBoxLayout(vertical=True, space_between=5)
        ball_speed_box.add(ball_speed_desc)
        ball_speed_box.add(ball_speed_hbox)
        self.slider_box.add(ball_speed_box)

        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.slider_box)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        self.manager.disable()
        arcade.get_window().show_view(MainMenuView())

    def updateState(self):
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

    def on_hide_view(self):
        self.state.manager.disable()


# ----------------------------
# High Scores State and View
# ----------------------------
class HighScoresState(GameState):
    def __init__(self):
        super().__init__("High Scores")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.back_button = arcade.gui.UIFlatButton(text="Back", width=100)
        self.back_button.on_click = self.on_click_back
        self.back_anchor = arcade.gui.UIAnchorLayout()
        self.back_anchor.add(anchor_x="left", anchor_y="top", child=self.back_button)
        self.manager.add(self.back_anchor)

        scores = (
            "High Scores:\n"
            "1. AAA - 10000\n"
            "2. BBB - 8000\n"
            "3. CCC - 6000"
        )
        self.info_label = arcade.gui.UILabel(
            text=scores,
            font_size=20,
            text_color=arcade.color.WHITE,
            multiline=True,
            width=400
        )
        self.center_anchor = arcade.gui.UIAnchorLayout()
        self.center_anchor.add(anchor_x="center", anchor_y="center", child=self.info_label)
        self.manager.add(self.center_anchor)

    def on_click_back(self, event):
        self.manager.disable()
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

    def on_hide_view(self):
        self.state.manager.disable()
