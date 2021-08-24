"""this module will contain the settings for alien invasion"""


class Settings:
    """the settings class for alien_Invasion"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        self.ship_speed = 1.5

        # bullets settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right -1 rep left
        self.fleet_direction = 1

