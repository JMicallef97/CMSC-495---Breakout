import arcade

# This class is the base class for all program states (where a state represents a particular
# function, like a menu or the actual gameplay), providing functions to update the state
# and draw the graphics of the program state.
class GameState:

    # defines the name of the game state
    nameState = ""

    # contains the sprite list, which the state's textures are added to in order
    # to be drawn to the screen
    stateSpriteList = arcade.SpriteList()

    # Constructor for the GameState class
    def __init__(self, stateName):
        self.nameState = stateName

    # Contains the code for updating the game state. Inheriting classes
    # should provide the update code.
    def updateState(self):
        pass

    # Used to draw the graphics of the game state to the screen
    def drawState(self):
        # draw the sprite list containing this game state's graphics
        self.stateSpriteList.draw()
