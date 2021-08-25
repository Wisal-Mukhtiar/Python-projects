"""module contain configuration about aliens in the game"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """this class will represent single alien on the fleet"""

    def __init__(self, ai_game):
        """init the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """return true if hit the edge """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move aliens"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
