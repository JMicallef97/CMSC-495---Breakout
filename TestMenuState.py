from platform import android_ver

import arcade
from Constants import Constants
from GameState import GameState
from InputManager import InputManager


# This class encapsulates code used to initialize, update, and draw the "Test Menu" class,
# which is used to test features. It is not intended to be part of the final game.
class TestMenuState(GameState):

    # represents the graphics of the test menu.
    graphic1 = None
    graphic2 = None
    isGraphicToggled = False

    def __init__(self):
        # initialize the parent class
        super().__init__("Test Menu")

        self.graphic1 = arcade.Sprite("Graphics/Button Outline.png")
        self.graphic1.center_x = 320
        self.graphic1.center_y = 200

        self.graphic2 = arcade.Sprite("Graphics/Button Outline.png")
        self.graphic2.center_x = 320
        self.graphic2.center_y = 250

        # add graphics to the parent class (GameState's) sprite list,
        # to be drawn in GameState.drawState().
        super().stateSpriteList.append(self.graphic1)
        super().stateSpriteList.append(self.graphic2)

    # Updates the test menu.
    def updateState(self):

        # KEYBOARD INPUT TEST CODE

        # check if the A/D keys are pressed (to move graphic 1 for keyboard testing)
        if InputManager.isKeyPressed[arcade.key.A]:
            # move graphic 1 left
            self.graphic1.center_x -= 2
        if InputManager.isKeyPressed[arcade.key.D]:
            # move graphic 1 left
            self.graphic1.center_x += 2

        # clamp graphic1 x and y bounds so the graphic can't disappear
        if self.graphic1.center_x < 0:
            self.graphic1.center_x = 0
        if self.graphic1.center_x > Constants.WINDOW_WIDTH:
            self.graphic1.center_x = Constants.WINDOW_WIDTH


        # MOUSE INPUT TEST CODE
        if (self.graphic2.rect.x - (self.graphic2.width / 2) < InputManager.mouseCoordX < self.graphic2.rect.right and
           self.graphic2.rect.bottom < InputManager.mouseCoordY < self.graphic2.rect.y + (self.graphic2.height / 2) and
           InputManager.isLeftMouseButtonPressed):

           # toggle the flag
           self.isGraphicToggled = not self.isGraphicToggled

           # adjust the graphic's color to indicate the click
           if self.isGraphicToggled:
               self.graphic2.color = arcade.color.RED
           else:
               self.graphic2.color = arcade.color.WHITE

           # reset the mouse press field to avoid buggy behavior
           InputManager.isLeftMouseButtonPressed = False