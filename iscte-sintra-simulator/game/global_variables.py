class GameVariables(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GameVariables, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Ensures __init__ runs only once
            self.initialized = True
            self.score = 4387438
            self.level = 1
            self.player_name = "Player1"

            self.screen_width = 1280
            self.screen_height = 720