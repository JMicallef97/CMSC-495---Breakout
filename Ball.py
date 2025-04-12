
import arcade
import math
import os

class Ball(arcade.Sprite):
    """
    Represents the ball in the Breakout game. Inherits from arcade.Sprite and handles movement,
    texture loading, collision with screen boundaries, and position updates.
    """

    def __init__(self, screen_width=640, screen_height=480, speed_difficulty: int = 1):
        """
        Initialize the Ball object with a texture, size, and movement properties.
        Loads the ball texture from the Graphics folder relative to this file.

        :param screen_width: The width of the game window.
        :param screen_height: The height of the game window.
        """
        # Store screen dimensions first
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed_difficulty = speed_difficulty

        # Construct full path to the ball texture
        current_dir = os.path.dirname(os.path.abspath(__file__))
        texture_path = os.path.normpath(os.path.join(current_dir, "Graphics", "Ball.png"))

        print("Loading texture from:", texture_path)

        # Check if the texture file exists
        if not os.path.exists(texture_path):
            raise FileNotFoundError(f"Texture not found at: {texture_path}")

        # Initialize the sprite with the texture
        super().__init__(texture_path, scale=0.5)

        # Define physical properties
        self.radius = self.width // 2
        self.center_x = self.screen_width // 2
        self.center_y = self.screen_height // 2
        self.change_x = 0
        self.change_y = 0

    def move_ball(self):
        """
        Update the ball's position based on its velocity and reverse direction
        if it hits the side or top walls of the screen.
        """
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounce off the left or right walls
        if self.center_x <= self.radius or self.center_x >= self.screen_width - self.radius:
            self.change_x *= -1

        # Bounce off the top wall
        if self.center_y >= self.screen_height - self.radius:
            self.change_y *= -1

    def apply_initial_velocity(self, angle_degrees: float):
        """
        Sets the initial ball velocity based on difficulty and launch angle.

        :param angle_degrees: Angle to launch the ball, in degrees (e.g., 45° to 135° range).
        """
        angle_rad = math.radians(angle_degrees)

        base_speed = 3
        max_boost = 4
        difficulty_scale = (self.speed_difficulty - 1) / 9  # Normalize: 1→0.0, 10→1.0
        speed = base_speed + max_boost * difficulty_scale

        self.change_x = speed * math.cos(angle_rad)
        self.change_y = speed * math.sin(angle_rad)