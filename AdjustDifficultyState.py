import arcade
import arcade.gui
from arcade.gui.widgets.slider import UISlider
from arcade.gui.events import UIOnChangeEvent
from GameState import GameState
from GameData import GameData
from GameView import GameView

# This class encapsulates code to set up and display the difficulty adjustment menu,
# providing event handlers for the menu controls (slider bars to adjust different
# difficulty settings).
class AdjustDifficultyState(GameState):
    def __init__(self):
        super().__init__("Adjust Difficulty")
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Back button to return to the main menu.
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
        self.paddle_width_slider = UISlider(
            value=GameData().difficulty_paddleWidth, width=300, height=50, min_value=1, max_value=10, step=1
        )
        paddle_width_value_label = arcade.gui.UILabel(
            text=f"{int(self.paddle_width_slider.value)}", font_size=16, text_color=arcade.color.WHITE
        )
        @self.paddle_width_slider.event("on_change")
        def on_change_pw(event: UIOnChangeEvent):
            paddle_width_value_label.text = f"{int(self.paddle_width_slider.value)}"
            paddle_width_value_label.fit_content()
            GameData().setPaddleWidthDifficulty(int(self.paddle_width_slider.value))
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
        self.paddle_speed_slider = UISlider(
            value=GameData().difficulty_paddleMoveSpeed, width=300, height=50, min_value=1, max_value=10, step=1
        )
        paddle_speed_value_label = arcade.gui.UILabel(
            text=f"{int(self.paddle_speed_slider.value)}", font_size=16, text_color=arcade.color.WHITE
        )
        @self.paddle_speed_slider.event("on_change")
        def on_change_ps(event: UIOnChangeEvent):
            paddle_speed_value_label.text = f"{int(self.paddle_speed_slider.value)}"
            paddle_speed_value_label.fit_content()
            GameData().difficulty_paddleMoveSpeed = int(self.paddle_speed_slider.value)
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
        self.ball_speed_slider = UISlider(
            value=GameData().difficulty_ballSpeed, width=300, height=50, min_value=1, max_value=10, step=1
        )
        ball_speed_value_label = arcade.gui.UILabel(
            text=f"{int(self.ball_speed_slider.value)}", font_size=16, text_color=arcade.color.WHITE
        )
        @self.ball_speed_slider.event("on_change")
        def on_change_bs(event: UIOnChangeEvent):
            ball_speed_value_label.text = f"{int(self.ball_speed_slider.value)}"
            ball_speed_value_label.fit_content()
            GameData().difficulty_ballSpeed = int(self.ball_speed_slider.value)
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
        # Print current difficulty levels to the console to test functionality.
        print(f"Current Difficulty Levels - Paddle Width: {GameData().difficulty_paddleWidth}, "
              f"Paddle Move Speed: {GameData().difficulty_paddleMoveSpeed}, "
              f"Ball Speed: {GameData().difficulty_ballSpeed}")
        self.manager.disable()
        import MainMenuState
        arcade.get_window().show_view(GameView(MainMenuState.MainMenuState()))

    def drawState(self):
        self.manager.draw()
