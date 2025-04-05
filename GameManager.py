import arcade
import math
import random
from game.Ball import Ball
from game.Paddle import Paddle
from game.Brick import Brick

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

        # Create main game objects
        self.paddle = Paddle(width)
        self.ball = Ball()

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

        # Input tracking
        self.holding_left = False
        self.holding_right = False

    def create_bricks(self) -> None:
        """
        Creates a 5-row by 10-column grid of bricks and adds them to the SpriteList.
        """
        brick_width = 60
        brick_height = 20
        rows = 5
        cols = 10
        x_offset = 60
        y_offset = 400

        for row in range(rows):
            for col in range(cols):
                brick_x = x_offset + col * brick_width
                brick_y = y_offset - row * brick_height
                brick = Brick(brick_x, brick_y)
                self.bricks.append(brick)

    def reset_game(self) -> None:
        """
        Resets the ball's position to the paddle after a life is lost.
        Ends the game if no lives remain.
        """
        self.ball.center_x = self.paddle.center_x
        ball_above_paddle = (self.paddle.height / 2) + (self.ball.height / 2)
        self.ball.center_y = self.paddle.center_y + ball_above_paddle
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

        # Handle continuous paddle movement
        if self.holding_left:
            self.paddle.move_left()
        if self.holding_right:
            self.paddle.move_right()

        # Keep ball attached to paddle before launch
        if self.ball_attached:
            self.ball.center_x = self.paddle.center_x
            ball_above_paddle = (self.paddle.height / 2) + (self.ball.height / 2)
            self.ball.center_y = self.paddle.center_y + ball_above_paddle
            return

        # Move the ball once it's launched
        self.ball.move_ball()

        # Check for collision with paddle
        if arcade.check_for_collision(self.ball, self.paddle):
            self.ball.change_y *= -1

        # Check for collision with bricks
        hit_list = arcade.check_for_collision_with_list(self.ball, self.bricks)
        if hit_list:
            brick = hit_list[0]
            brick.destroy()
            self.ball.change_y *= -1
            self.score += 10

        # Ball fell below the screen
        if self.ball.center_y <= 0:
            self.reset_game()

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """
        Handles key press events to control paddle movement and toggle pause/quit.
        """
        if symbol == arcade.key.A:
            self.holding_left = True
        elif symbol == arcade.key.D:
            self.holding_right = True
        elif symbol == arcade.key.P:
            self.game_paused = not self.game_paused
        elif symbol == arcade.key.Q:
            self.quit_game()

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        """
        Handles key release events to stop paddle movement.
        """
        if symbol == arcade.key.A:
            self.holding_left = False
        elif symbol == arcade.key.D:
            self.holding_right = False

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        """
        Handles mouse click to launch the ball from the paddle with a random upward angle.
        """
        if self.ball_attached:
            self.ball_attached = False

            # Choose a random upward angle between 30° and 150°
            angle_deg = random.uniform(30, 150)
            angle_rad = math.radians(angle_deg)

            speed = 5
            self.ball.change_x = speed * math.cos(angle_rad)
            self.ball.change_y = speed * math.sin(angle_rad)

    @staticmethod
    def quit_game() -> None:
        """
        Quits the game and closes the window.
        """
        print("Exiting Game")
        arcade.close_window()

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
