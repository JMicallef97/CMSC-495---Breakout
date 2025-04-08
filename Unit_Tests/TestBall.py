from Ball import Ball

class TestBall:
    """
    Unit tests for the Ball class used in the Breakout game.
    These tests verify the Ball's initialization and movement behavior.
    """

    def test_initial_position_and_velocity(self):
        """
        Test that a newly created Ball has zero velocity.
        This ensures the ball starts in a stationary state before being launched.
        """
        ball = Ball()
        # Check if ball initializes with zero velocity
        assert ball.change_x == 0
        assert ball.change_y == 0

    def test_move_ball_updates_position(self):
        """
        Test that the ball's position updates correctly based on its velocity.
        This checks that the move_ball method applies velocity to position accurately.
        """
        ball = Ball()
        ball.center_x = 100
        ball.center_y = 200
        ball.change_x = 5
        ball.change_y = -3

        ball.move_ball()

        assert ball.center_x == 105
        assert ball.center_y == 197
