import arcade
import os

class Brick(arcade.Sprite):
    """
    Represents a single brick in the Breakout game.
    Inherits from arcade.Sprite and handles its own initialization and removal.
    """
    def __init__(self, x, y,):
        """
        Initialize a Brick object at the given (x, y) position.
        Loads the brick texture from the Graphics folder relative to this file.

        :param x: The horizontal (center_x) position of the brick.
        :param y: The vertical (center_y) position of the brick.
        """
        # Construct full path to the brick texture
        current_dir = os.path.dirname(os.path.abspath(__file__))
        texture_path = os.path.normpath(os.path.join(current_dir, "Graphics", "Brick.png"))

        if not os.path.exists(texture_path):
            raise FileNotFoundError(f"Brick texture not found at: {texture_path}")

        # Initialize the sprite with the brick texture
        super().__init__(texture_path, scale=1)

        # Set the position of the brick
        self.center_x = x
        self.center_y = y

    def destroy(self):
        """
        Removes the brick from all sprite lists, effectively destroying it.
        Called when the brick is hit by the ball.
        """
        self.remove_from_sprite_lists()
