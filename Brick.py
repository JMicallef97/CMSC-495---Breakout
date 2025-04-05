import arcade
import os

class Brick(arcade.Sprite):
    def __init__(self, x, y):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        texture_path = os.path.normpath(os.path.join(current_dir, "Graphics", "Brick.png"))

        print("Loading brick texture from:", texture_path)
        if not os.path.exists(texture_path):
            raise FileNotFoundError(f"Brick texture not found at: {texture_path}")

        super().__init__(texture_path, scale=0.75)

        self.center_x = x
        self.center_y = y

    def destroy(self):
        self.remove_from_sprite_lists()
