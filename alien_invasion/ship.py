"""module for the ship settings"""
import pygame


class Ship:
    """setting for the ship in this class"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        # loading the ship image and getting its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start the new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the horizontal position of the ship
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Drawing the ship and its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centers the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
