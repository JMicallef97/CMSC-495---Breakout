import arcade
import math
import random

from Ball import Ball
from Paddle import Paddle
from Brick import Brick
from InputManager import InputManager
from GameData import GameData

class GameManager:
    """
    Manages the core gameplay elements for the Breakout game, including
    paddle and ball movement, brick generation, scoring, and input handling.
    """

    def __init__(self, width: int, height: int):
        """
        Initialize the game manager with the screen dimensions and game state.
        """
        self.width = width
        self.height = height

        # Retrieve difficulty settings
        paddle_width_difficulty = GameData().getPaddleWidthDifficulty()
        paddle_speed_difficulty = GameData().getPaddleMoveSpeedDifficulty()
        ball_speed_difficulty = GameData().getBallSpeedDifficulty()

        # Create main game objects
        self.paddle = Paddle(width, paddle_width_difficulty, paddle_speed_difficulty)
        self.ball = Ball(width, height, ball_speed_difficulty)

        # SpriteLists for efficient drawing
        self.paddle_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.bricks = arcade.SpriteList()

        self.paddle_list.append(self.paddle)
        self.ball_list.append(self.ball)

        self.create_bricks()

        # Game state variables
        self.score = 0
        self.lives = 3
        self.game_paused = False
        self.ball_attached = True  # Ball starts on paddle

    def create_bricks(self) -> None:
        """
        Creates a 5-row by 10-column grid of bricks and adds them to the SpriteList.
        """
        brick_width = 64
        brick_height = 32
        rows = 5
        cols = 10

        # Compute horizontal offset to center the full row of bricks
        total_brick_width = cols * brick_width
        x_offset = (self.width - total_brick_width) // 2
        y_offset = self.height - 100  # Starting vertical position

        for row in range(rows):
            for col in range(cols):
                brick_x = x_offset + col * brick_width + brick_width // 2
                brick_y = y_offset - row * brick_height - brick_height // 2
                brick = Brick(brick_x, brick_y)
                self.bricks.append(brick)

    def reset_game(self) -> None:
        """
        Resets the ball's position to the paddle after a life is lost.
        Ends the game if no lives remain.
        """
        self.ball.center_x = self.paddle.center_x
        self.ball.center_y = self.paddle.center_y + (self.paddle.height / 2) + (self.ball.height / 2)
        self.ball.change_x = 0
        self.ball.change_y = 0
        self.lives -= 1
        self.ball_attached = True

        if self.lives <= 0:
            self.game_over()

    def game_over(self) -> None:
        """
        Ends the game and closes the window.
        """
        print(f"Game Over! Final Score: {self.score}")
        arcade.close_window()

    def update(self) -> None:
        """
        Updates the game state every frame: handles paddle movement, ball motion,
        collision detection, and game logic.
        """
        if self.game_paused:
            return

        # Handle input via InputManager
        if InputManager.isKeyPressed.get(arcade.key.A, False):
            self.paddle.move_left()
        if InputManager.isKeyPressed.get(arcade.key.D, False):
            self.paddle.move_right()
        if InputManager.isKeyPressed.get(arcade.key.P, False):
            self.game_paused = not self.game_paused
            InputManager.isKeyPressed[arcade.key.P] = False  # prevent repeated toggling
        if InputManager.isKeyPressed.get(arcade.key.Q, False):
            print("Quitting game.")
            arcade.close_window()

        # Keep ball attached to paddle before launch
        if self.ball_attached:
            self.ball.center_x = self.paddle.center_x
            self.ball.center_y = self.paddle.center_y + (self.paddle.height / 2) + (self.ball.height / 2)

            # Launch the ball if mouse button is pressed
            if InputManager.isLeftMouseButtonPressed:
                self.launch_ball()
            return

        # Move the ball
        self.ball.move_ball()

        # Paddle collision
        if arcade.check_for_collision(self.ball, self.paddle):
            self.ball.change_y *= -1

        # Brick collision
        hit_list = arcade.check_for_collision_with_list(self.ball, self.bricks)
        if hit_list:
            hit_list[0].destroy()
            self.ball.change_y *= -1
            self.score += 10

        # Ball fell below screen
        if self.ball.center_y <= 0:
            self.reset_game()

    def launch_ball(self) -> None:
        """
        Launches the ball at a random upward angle from the paddle.
        """
        self.ball_attached = False
        angle = random.uniform(30, 150)
        self.ball.apply_initial_velocity(angle)

    def draw(self) -> None:
        """
        Draws all game elements including the paddle, ball, bricks, score, and lives.
        Also shows a launch message if the ball is not yet in play.
        """
        self.paddle_list.draw()
        self.ball_list.draw()
        self.bricks.draw()

        # Draw score and lives
        arcade.draw_text(f"Score: {self.score}", 10, self.height - 30, arcade.color.WHITE, 14)
        arcade.draw_text(f"Lives: {self.lives}", self.width - 100, self.height - 30, arcade.color.WHITE, 14)

        # Launch prompt if ball is still attached
        if self.ball_attached:
            arcade.draw_text("Click to launch!",
                             self.width // 2 - 80, self.height // 2,
                             arcade.color.LIGHT_GRAY, 16)
