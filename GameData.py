# This class defines an object used to store data used by the game, such as difficulty
# settings, game score, et cetera. It is meant to persistently store data across different
# menus and game sessions.

class GameData:

    # Stores the difficulty setting affecting the width of the paddle. Should be a value
    # between 1 and 10, with 1 being the easiest and 10 being the hardest. Defaults to 1.
    difficulty_paddleWidth = 1

    # Stores the difficulty setting affecting the speed of the ball. Should be a value
    # between 1 and 10, with 1 being the easiest and 10 being the hardest. Defaults to 1.
    difficulty_ballSpeed = 1

    # Stores the difficulty setting affecting the movement speed of the paddle. Should be
    # a value between 1 and 10, with 1 being the easiest and 10 being the hardest.
    # Defaults to 1.
    difficulty_paddleMoveSpeed = 1

    # Stores the singleton instance of this class.
    _instance = None

    # This function ensures that this class remains a singleton (only 1 instance of it
    # exists throughout the game) since Python's import system is terrible and other, more
    # logical approaches don't work.
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameData, cls).__new__(cls)
        return cls._instance

    # Constructor for the GameData class, initializes the starting values
    # for each variable.
    def __init__(self, value=1):

        # Ensure class will not be reinitialized
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True

            # Set default difficulty settings
            self.difficulty_paddleWidth = 1
            self.difficulty_ballSpeed = 1
            self.difficulty_paddleMoveSpeed = 1

    # Sets the paddle width difficulty in this GameData instance.
    def setPaddleWidthDifficulty(self, newWidth):
        self.difficulty_paddleWidth = newWidth

    # Gets the paddle width difficulty in this GameData instance.
    def getPaddleWidthDifficulty(self):
        return self.difficulty_paddleWidth

    # Sets the ball speed difficulty in this GameData instance.
    def setBallSpeedDifficulty(self, newBallSpeed):
        self.difficulty_ballSpeed = newBallSpeed

    # Gets the ball speed difficulty in this GameData instance.
    def getBallSpeedDifficulty(self):
        return self.difficulty_ballSpeed

    # Sets the paddle movement speed difficulty in this GameData instance.
    def setPaddleMoveSpeedDifficulty(self, newPaddleSpeed):
        self.difficulty_paddleMoveSpeed = newPaddleSpeed

    # Gets the paddle movement speed difficulty in this GameData instance.
    def getPaddleMoveSpeedDifficulty(self):
        return self.difficulty_paddleMoveSpeed