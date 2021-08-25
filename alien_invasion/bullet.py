"""module contain configuaration of the bullets fired by the ship"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """this class manage bullets fired from ship"""

    def __init__(self, ai_game):
        """create bullet object at current ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up the screen """
        # update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # update the rect positoin
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
