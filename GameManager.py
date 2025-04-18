import arcade
import random

from Ball import Ball
from GameView import GameView
from Paddle import Paddle
from Brick import Brick
from InputManager import InputManager
from GameData import GameData

class GameManager:
    """
    Manages the core gameplay loop and state transitions for the Breakout game.
    Handles paddle movement, ball control, collision detection, scoring,
    difficulty integration, pause and quit logic, and visual rendering.
    """

    def __init__(self, width: int, height: int):
        """
        Initialize the GameManager with the screen dimensions and setup initial game state.

        :param width: Width of the game window.
        :param height: Height of the game window.
        """
        self.width = width
        self.height = height

        # Retrieve difficulty settings from GameData
        paddle_width_difficulty = GameData().getPaddleWidthDifficulty()
        paddle_speed_difficulty = GameData().getPaddleMoveSpeedDifficulty()
        ball_speed_difficulty = GameData().getBallSpeedDifficulty()

        # Create paddle and ball with difficulty applied
        self.paddle = Paddle(width, paddle_width_difficulty, paddle_speed_difficulty)
        self.ball = Ball(width, height, ball_speed_difficulty)

        # Sprite containers for drawing and updates
        self.paddle_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.bricks = arcade.SpriteList()

        self.paddle_list.append(self.paddle)
        self.ball_list.append(self.ball)

        # Populate the brick grid
        self.create_bricks()

        # Initialize game state variables
        self.score = 0
        self.lives = 3
        self.game_paused = False
        self.ball_attached = True
        self.quit_pending = False

    def create_bricks(self) -> None:
        """
        Create a grid of bricks and add them to the bricks SpriteList.
        """
        brick_width = 64
        brick_height = 32
        rows = 5
        cols = 10

        total_brick_width = cols * brick_width
        x_offset = (self.width - total_brick_width) // 2
        y_offset = self.height - 100

        for row in range(rows):
            for col in range(cols):
                brick_x = x_offset + col * brick_width + brick_width // 2
                brick_y = y_offset - row * brick_height - brick_height // 2
                brick = Brick(brick_x, brick_y)
                self.bricks.append(brick)

    def reset_game(self) -> None:
        """
        Resets the ball to the paddle position and decrements a life.
        Ends the game if no lives remain.
        """
        self.ball.center_x = self.paddle.center_x
        self.ball.center_y = self.paddle.center_y + (self.paddle.height / 2) + (self.ball.height / 2)
        self.ball.change_x = 0
        self.ball.change_y = 0
        self.lives -= 1
        self.ball_attached = True
        self.quit_pending = False  # Reset quit state

        if self.lives <= 0:
            self.game_over()

    def game_over(self) -> None:
        """
        Handles game over logic: saving score to file and transitioning to the GameOver state.
        """
        final_score = self.score
        print(f"Game Over! Final Score: {final_score}")

        try:
            import datetime
            now = datetime.datetime.now()
            with open("highscores.txt", "a") as f:
                f.write(f"{final_score} - {now.strftime('%Y-%m-%d %H:%M')}\n")
        except Exception as e:
            print("Error writing score to file:", e)

        from GameOverState import GameOverState
        arcade.get_window().show_view(GameView(GameOverState(final_score)))
        self.quit_pending = False

    def update(self) -> None:
        """
        Called every frame. Handles input, game state updates,
        ball movement, and collision detection.
        """
        # Handle pause toggle
        if InputManager.isKeyPressed.get(arcade.key.P, False):
            if self.quit_pending:
                self.quit_pending = False
                print("Quit canceled. Resuming game.")
            else:
                self.game_paused = not self.game_paused
            InputManager.isKeyPressed[arcade.key.P] = False

        # Handle quit toggle
        if InputManager.isKeyPressed.get(arcade.key.Q, False):
            if self.quit_pending:
                print("Exiting game...")
                arcade.exit()
            else:
                print("Press Q again to quit, or P to resume.")
                self.quit_pending = True
                self.game_paused = True
            InputManager.isKeyPressed[arcade.key.Q] = False

        # Pause game logic if paused
        if self.game_paused:
            return

        # Paddle movement
        if InputManager.isKeyPressed.get(arcade.key.A, False):
            self.paddle.move_left()
        if InputManager.isKeyPressed.get(arcade.key.D, False):
            self.paddle.move_right()

        # Keep ball attached before launch
        if self.ball_attached:
            self.ball.center_x = self.paddle.center_x
            self.ball.center_y = self.paddle.center_y + (self.paddle.height / 2) + (self.ball.height / 2)

            if InputManager.isLeftMouseButtonPressed:
                self.launch_ball()
            return

        # Ball movement
        self.ball.move_ball()

        # Ball-paddle collision
        if arcade.check_for_collision(self.ball, self.paddle) and self.ball.change_y < 0:
            self.ball.deflect_off_paddle(self.paddle)

        # Ball-brick collision
        hit_list = arcade.check_for_collision_with_list(self.ball, self.bricks)
        if hit_list:
            hit_list[0].destroy()
            self.ball.change_y *= -1
            self.score += 10

        # Ball falls off screen
        if self.ball.center_y <= 0:
            self.reset_game()

    def launch_ball(self) -> None:
        """
        Launch the ball at a random upward angle when the player clicks to start.
        """
        self.ball_attached = False
        angle = random.uniform(30, 150)
        self.ball.apply_initial_velocity(angle)

    def draw(self) -> None:
        """
        Draws all gameplay elements: paddle, ball, bricks, score, lives,
        and visual overlays for pause or quit state.
        """
        self.paddle_list.draw()
        self.ball_list.draw()
        self.bricks.draw()

        # Draw score and lives
        arcade.draw_text(f"Score: {self.score}", 10, self.height - 30, arcade.color.WHITE, 14)
        arcade.draw_text(f"Lives: {self.lives}", self.width - 100, self.height - 30, arcade.color.WHITE, 14)

        # Ball launch message
        if self.ball_attached:
            arcade.draw_text("Click to launch!",
                             self.width // 2 - 80, self.height // 2,
                             arcade.color.LIGHT_GRAY, 16)

        brick_base_y = self.height - 100 - (5 * 32) + 32 // 2  # bottom row of bricks
        paddle_brick_midpoint = (self.paddle.center_y + brick_base_y) // 2

        # Pause message
        if self.game_paused and not self.quit_pending:
            # First line: "PAUSED"
            arcade.draw_text("PAUSED",
                             self.width // 2,
                             paddle_brick_midpoint + 16,
                             arcade.color.WHITE, 20,
                             anchor_x="center")

            # Second line: "Press P to resume"
            arcade.draw_text("Press P to resume",
                             self.width // 2,
                             paddle_brick_midpoint - 12,
                             arcade.color.WHITE, 16,
                             anchor_x="center")

        # Quit confirmation message
        if self.quit_pending:
            arcade.draw_text("QUIT GAME?",
                             self.width // 2,
                             paddle_brick_midpoint + 16,
                             arcade.color.WHITE, 20,
                             anchor_x="center")

            # Second line: "Press P to resume"
            arcade.draw_text("Press Q to quit, press P to resume",
                             self.width // 2,
                             paddle_brick_midpoint - 12,
                             arcade.color.WHITE, 16,
                             anchor_x="center")
