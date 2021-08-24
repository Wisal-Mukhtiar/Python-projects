"""this module will contain the settings for alien invasion"""


class Settings:
    """the settings class for alien_Invasion"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        self.ship_speed = 1.5

        # bullets settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3