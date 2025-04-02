import arcade
from Constants import Constants
from GameState import GameState
from InputManager import InputManager

class StartMenuState(GameState):
    def __init__(self):
        super().__init__("Main Menu")
        self.options = ["Start Game", "How To Play", "High Scores"]
        self.selected_option = 0
        # Prepare bounding boxes and text objects.
        self.option_boxes = []  # List of tuples: (left, right, bottom, top)
        self.menu_texts = []    # arcade.Text objects for each option
        self.title_text = arcade.Text(
            "Main Menu",
            Constants.WINDOW_WIDTH / 2,
            Constants.WINDOW_HEIGHT - 100,
            arcade.color.WHITE,
            40,
            anchor_x="center"
        )
        self.setup_options()

    def setup_options(self):
        center_x = Constants.WINDOW_WIDTH // 2
        start_y = Constants.WINDOW_HEIGHT // 2 + 50
        gap = 50
        box_width = 200
        box_height = 40
        self.option_boxes = []
        self.menu_texts = []
        for i, option in enumerate(self.options):
            center_y = start_y - i * gap
            left = center_x - box_width // 2
            right = center_x + box_width // 2
            bottom = center_y - box_height // 2
            top = center_y + box_height // 2
            self.option_boxes.append((left, right, bottom, top))
            text = arcade.Text(
                option,
                center_x,
                center_y,
                arcade.color.WHITE,
                24,
                anchor_x="center",
                anchor_y="center"
            )
            self.menu_texts.append(text)

    def updateState(self):
        # --- Mouse Input ---
        if InputManager.isLeftMouseButtonPressed:
            x = InputManager.mouseCoordX
            y = InputManager.mouseCoordY
            for idx, (left, right, bottom, top) in enumerate(self.option_boxes):
                if left <= x <= right and bottom <= y <= top:
                    self.select_option(idx)
                    InputManager.isLeftMouseButtonPressed = False
                    break

    def drawState(self):
        self.title_text.draw()
        for idx, text in enumerate(self.menu_texts):
            left, right, bottom, top = self.option_boxes[idx]
            if idx == self.selected_option:
                arcade.draw_rectangle_filled(
                    (left + right) / 2,
                    (bottom + top) / 2,
                    right - left,
                    top - bottom,
                    arcade.color.GRAY
                )
                text.color = arcade.color.YELLOW
            else:
                text.color = arcade.color.WHITE
            text.draw()

    def select_option(self, index):
        window = arcade.get_window()
        if index == 0:
            window.show_view(StartGameStateView())
        elif index == 1:
            window.show_view(HowToPlayStateView())
        elif index == 2:
            window.show_view(HighScoresStateView())


class SubMenuState(GameState):
    def __init__(self, title):
        super().__init__(title)
        self.title = title
        self.screen_text = arcade.Text(
            f"{self.title} Screen",
            Constants.WINDOW_WIDTH / 2,
            Constants.WINDOW_HEIGHT / 2,
            arcade.color.WHITE,
            24,
            anchor_x="center",
            anchor_y="center"
        )
        self.back_text = arcade.Text(
            "<- Back",
            10,
            Constants.WINDOW_HEIGHT - 40,
            arcade.color.WHITE,
            20
        )

    def updateState(self):
        # Mouse "Back" Button
        if InputManager.isLeftMouseButtonPressed:
            if 10 <= InputManager.mouseCoordX <= 100 and Constants.WINDOW_HEIGHT - 60 <= InputManager.mouseCoordY <= Constants.WINDOW_HEIGHT - 20:
                arcade.get_window().show_view(TestMenuStateView())
                InputManager.isLeftMouseButtonPressed = False

    def drawState(self):
        self.screen_text.draw()
        self.back_text.draw()

class TestMenuStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = TestMenuState()

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_key_press(self, key, modifiers):
        # Forward key presses to InputManager.
        if key in InputManager.isKeyPressed:
            InputManager.isKeyPressed[key] = True

    def on_key_release(self, key, modifiers):
        if key in InputManager.isKeyPressed:
            InputManager.isKeyPressed[key] = False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            InputManager.isLeftMouseButtonPressed = True
            InputManager.mouseCoordX = x
            InputManager.mouseCoordY = y


class StartGameStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = SubMenuState("Start Game")

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_key_press(self, key, modifiers):
        if key in InputManager.isKeyPressed:
            InputManager.isKeyPressed[key] = True

    def on_key_release(self, key, modifiers):
        if key in InputManager.isKeyPressed:
            InputManager.isKeyPressed[key] = False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            InputManager.isLeftMouseButtonPressed = True
            InputManager.mouseCoordX = x
            InputManager.mouseCoordY = y


class HowToPlayStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = SubMenuState("How To Play")

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_key_press(self, key, modifiers):
        if key in InputManager.isKeyPressed:
            InputManager.isKeyPressed[key] = True

    def on_key_release(self, key, modifiers):
        if key in InputManager.isKeyPressed:
            InputManager.isKeyPressed[key] = False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            InputManager.isLeftMouseButtonPressed = True
            InputManager.mouseCoordX = x
            InputManager.mouseCoordY = y


class HighScoresStateView(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = SubMenuState("High Scores")

    def on_draw(self):
        self.clear()
        self.state.drawState()

    def on_update(self, delta_time):
        self.state.updateState()

    def on_key_press(self, key, modifiers):
        if key in InputManager.isKeyPressed:
            InputManager.isKeyPressed[key] = True

    def on_key_release(self, key, modifiers):
        if key in InputManager.isKeyPressed:
            InputManager.isKeyPressed[key] = False

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            InputManager.isLeftMouseButtonPressed = True
            InputManager.mouseCoordX = x
            InputManager.mouseCoordY = y