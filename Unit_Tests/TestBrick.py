import pytest
from Brick import Brick

class TestBrick:
    """
    Unit tests for the Brick class, covering initialization and destruction logic.
    """

    def test_initial_position(self):
        """
        Verify that a brick initializes at the given coordinates.
        """
        brick = Brick(100, 200)
        assert brick.center_x == 100
        assert brick.center_y == 200

    def test_destroy_runs_without_error(self):
        """
        Confirm that calling destroy() does not raise an error.
        """
        brick = Brick(100, 200)
        try:
            brick.destroy()
        except Exception as e:
            pytest.fail(f"destroy() raised an exception: {e}")