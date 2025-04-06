import arcade
import os

class Ball(arcade.Sprite):
    """
    Represents the ball in the Breakout game. Inherits from arcade.Sprite and handles movement,
    texture loading, collision with screen boundaries, and position updates.
    """
    def __init__(self):
        """
        Initialize the Ball object with a texture, size, and movement properties.
        Loads the ball texture from the Graphics folder relative to this file.
        """
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
        self.center_x = 400  # Initial X position
        self.center_y = 300  # Initial Y position
        self.change_x = 4    # Horizontal speed
        self.change_y = 4    # Vertical speed

    def move_ball(self):
        """
        Update the ball's position based on its velocity and reverse direction
        if it hits the side or top walls of the screen.
        """
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounce off the left or right walls
        if self.center_x <= self.radius or self.center_x >= 800 - self.radius:
            self.change_x *= -1

        # Bounce off the top wall
        if self.center_y >= 600 - self.radius:
            self.change_y *= -1
