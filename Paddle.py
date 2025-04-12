import arcade
import os

class Paddle(arcade.Sprite):
    """
    Represents the player's paddle in the Breakout game.
    Inherits from arcade.Sprite and handles movement and boundary constraints.
    """
    def __init__(self, screen_width: int, width_difficulty: int = 1, speed_difficulty: int = 1):
        """
        Initialize the Paddle object with a texture, position, and movement speed.
        The paddle starts centered horizontally and near the bottom of the screen.

        :param screen_width: The width of the game screen, used to constrain paddle movement.
        """
        # Construct full path to the paddle texture
        current_dir = os.path.dirname(os.path.abspath(__file__))
        texture_path = os.path.normpath(os.path.join(current_dir, "Graphics", "Paddle.png"))

        print("Loading paddle texture from:", texture_path)

        # Check if the texture file exists
        if not os.path.exists(texture_path):
            raise FileNotFoundError(f"Paddle texture not found at: {texture_path}")

        # Initialize the sprite with the paddle texture
        super().__init__(texture_path, scale=0.75)

        # Store screen width for movement limits
        self.screen_width = screen_width

        # Scale paddle width inversely by difficulty
        base_width = 150
        width_scale = max(1, min(width_difficulty, 10))  # Clamp between 1 and 10
        self.width = int(base_width * (1.0 - 0.06 * (width_scale - 1)))  # ~6% reduction per level

        # Scale movement speed proportionally by difficulty
        base_speed = 4
        self.speed = base_speed + (speed_difficulty - 1) * 0.6

        # Set initial position and movement speed
        self.center_x = screen_width // 2
        self.center_y = 50  # Near bottom of screen

    def move_left(self):
        """
        Move the paddle to the left by its speed value,
        stopping at the left edge of the screen.
        """
        self.center_x = max(self.width // 2, self.center_x - self.speed)

    def move_right(self):
        """
        Move the paddle to the right by its speed value,
        stopping at the right edge of the screen.
        """
        self.center_x = min(self.screen_width - self.width // 2, self.center_x + self.speed)
