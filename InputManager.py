# This class is used to store user input data, which will be processed by the
# active program/game state.
class InputManager:
    # -Used to store the state of the left mouse button. True if the button is pressed, false
    #  if not.
    isLeftMouseButtonPressed = False

    # -A dictionary which is used to store the state of the keyboard, by recording whether keys
    #  are pressed or released. The dictionary keys are the key codes of the characters being
    #  pressed (in the arcade.Keys enum), with the values being a boolean indicating if the key is
    #  being pressed (true) or not. To check if a key is pressed or released, check the value of
    #  the dictionary whose key corresponds to the arcade.key enum entry corresponding to the key
    #  (for example, arcade.key.A for the 'A' key).
    isKeyPressed = {}

    # Stores the X coordinate of the mouse.
    mouseCoordX = 0

    # Stores the Y coordinate of the mouse.
    mouseCoordY = 0