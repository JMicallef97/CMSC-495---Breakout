import arcade
import os

class Paddle(arcade.Sprite):
    def __init__(self, screen_width: int):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        texture_path = os.path.normpath(os.path.join(current_dir, "Graphics", "Paddle.png"))

        print("Loading paddle texture from:", texture_path)
        if not os.path.exists(texture_path):
            raise FileNotFoundError(f"Paddle texture not found at: {texture_path}")

        super().__init__(texture_path, scale=0.75)

        self.screen_width = screen_width
        self.center_x = screen_width // 2
        self.center_y = 50
        self.speed = 6

    def move_left(self):
        self.center_x = max(self.width // 2, self.center_x - self.speed)

    def move_right(self):
        self.center_x = min(self.screen_width - self.width // 2, self.center_x + self.speed)
