import arcade
import os

class Ball(arcade.Sprite):
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        texture_path = os.path.normpath(os.path.join(current_dir, "Graphics", "Ball.png"))

        print("Loading texture from:", texture_path)
        if not os.path.exists(texture_path):
            raise FileNotFoundError(f"Texture not found at: {texture_path}")

        # ✅ This is now all you need
        super().__init__(texture_path, scale=0.5)

        # Set up properties
        self.radius = self.width // 2
        self.center_x = 400
        self.center_y = 300
        self.change_x = 4
        self.change_y = 4

    def move_ball(self):
        """Updates the ball's position and handles wall collisions."""
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounce off side walls
        if self.center_x <= self.radius or self.center_x >= 800 - self.radius:
            self.change_x *= -1

        # Bounce off top wall
        if self.center_y >= 600 - self.radius:
            self.change_y *= -1
