from GameState import GameState
from StartMenuState import StartMenuState
from TestMenuState import TestMenuState


class GameStateManager:

    # array of GameState objects, which contains the states of the game. Populated
    # in the GameStateManager constructor.
    programGameStates = {}

    # Stores a reference to the active game state
    activeGameState = None

    # This function is used to initialize the different game state objects.
    def initGameStates(self):
        # Initialize the game states

        # Test Menu (used to test different features, will not be part of the final game)
        self.programGameStates["Test Menu"] = TestMenuState()

        # Main Menu (the main menu of the game)
        self.programGameStates["Main Menu"] = StartMenuState()

        # etc.. add other game states (game, game over, high score, etc) here

    # This function allows the caller to manually set the game state by name (IE, to set
    # the game state to main menu, call this function with "Main Menu" as the argument).
    # If the string passed to the function doesn't correspond to a game state (IE, None
    # or a blank string), nothing will happen. An error message will be printed to the console.
    # Otherwise, the game state will be printed to the console (for debugging purposes).
    def setGameState(self, newStateName):
        # Ensure that newStateName is valid
        if newStateName in self.programGameStates:
            # change the state to the requested menu
            self.activeGameState = self.programGameStates[newStateName]
            # print the state name to the menu
            print("Switched game state to '" + newStateName + "'.")
        else:
            # print console message with error
            print("Cannot manually set game state! Game state '"'' + newStateName + "'"' is not valid!')

    # This function updates the active game state.
    def updateActiveGameState(self):
        # update the active game state
        self.activeGameState.updateState()

    # This function draws the graphics of the active game state to the game window.
    def drawActiveGameState(self):
        # draw the active game state
        self.activeGameState.drawState()
