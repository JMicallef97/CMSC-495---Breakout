import arcade
from InputManager import InputManager

class TestInputManager:
    """
    Unit tests for the InputManager class, which handles input state tracking
    for the Breakout game. These tests validate key presses, mouse state, and
    mouse coordinate tracking.
    """

    def test_default_states(self):
        """
        Test that the default input states are correctly initialized.
        Ensures no keys or mouse buttons are active and mouse coordinates are at (0, 0).
        """
        assert InputManager.isLeftMouseButtonPressed is False
        assert InputManager.isKeyPressed == {}
        assert InputManager.mouseCoordX == 0
        assert InputManager.mouseCoordY == 0

    def test_key_press_tracking(self):
        """
        Test that key press states are correctly recorded in the isKeyPressed dictionary.
        This simulates pressing and releasing a specific key (A key).
        """
        InputManager.isKeyPressed[arcade.key.A] = True
        assert InputManager.isKeyPressed.get(arcade.key.A) is True
        InputManager.isKeyPressed[arcade.key.A] = False
        assert InputManager.isKeyPressed.get(arcade.key.A) is False

    def test_mouse_button_tracking(self):
        """
        Test that the left mouse button press state is correctly updated.
        Simulates pressing and releasing the left mouse button.
        """
        InputManager.isLeftMouseButtonPressed = True
        assert InputManager.isLeftMouseButtonPressed is True
        InputManager.isLeftMouseButtonPressed = False
        assert InputManager.isLeftMouseButtonPressed is False

    def test_mouse_coordinates(self):
        """
        Test that the mouse coordinates are correctly tracked.
        Simulates moving the mouse to a specific position on the screen.
        """
        InputManager.mouseCoordX = 150
        InputManager.mouseCoordY = 300
        assert InputManager.mouseCoordX == 150
        assert InputManager.mouseCoordY == 300
