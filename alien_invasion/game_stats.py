class GameStats:
    """Track statistics for alien Invasion"""

    def __init__(self, ai_game):
        """init the stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # start the game in an active state
        self.game_active = False

        # scores
        self.score = 0
        self.level = 1

        # high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """init the statistics that can change during the game """
        self.ships_left = self.settings.ship_limit
