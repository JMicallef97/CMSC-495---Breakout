import pytest
from Paddle import Paddle

SCREEN_WIDTH = 800

class TestPaddle:
    """
    Unit tests for the Paddle class used in the Breakout game.
    These tests verify paddle initialization and horizontal movement behavior.
    """

    def test_initial_position_and_size(self):
        """
        Test that the paddle is initialized with the correct position and attributes.
        Ensures it's centered horizontally, placed near the bottom of the screen,
        and has a 'speed' attribute for movement.
        """
        paddle = Paddle(SCREEN_WIDTH)
        assert paddle.center_x == SCREEN_WIDTH // 2
        assert paddle.center_y == 50
        assert hasattr(paddle, "speed")

    def test_move_left_decreases_position(self):
        """
        Test that calling move_left() causes the paddle to move to the left.
        Validates that the x-coordinate decreases appropriately.
        """
        paddle = Paddle(SCREEN_WIDTH)
        paddle.center_x = 400
        paddle.move_left()
        assert paddle.center_x < 400

    def test_move_right_increases_position(self):
        """
        Test that calling move_right() causes the paddle to move to the right.
        Validates that the x-coordinate increases appropriately.
        """
        paddle = Paddle(SCREEN_WIDTH)
        paddle.center_x = 400
        paddle.move_right()
        assert paddle.center_x > 400
