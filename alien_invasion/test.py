"""the main module"""

import sys

from time import sleep

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

from game_stats import GameStats


class AlienInvasion:
    """this class contain the overall assets of the game"""

    def __init__(self):
        """initalize and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien_Invasion")

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        """create the fleet of aliens"""
        # make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows of aliens that fits on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        # create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        # create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def run_game(self):
        """start the main loop for game and events"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """responds to pressed key events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Creating new bullet and add it to the bullet group """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """respond to released key events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """update the bullets position and get rid of old ones"""
        self.bullets.update()

        # get rid of the bullets that disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        # check for any bullet and alien if hit and get rid of both
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """check if the fleet is at an edge,
        then update the positions of aliens accordingly """
        self._check_fleet_edges()
        self.aliens.update()

        # alien and ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship hit by the aliens"""

        if self.stats.ships_left > 0 :
            # decrement ships_left
            self.stats.ships_left -= 1

            # get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

            # pause the game for a while
            sleep(1)

        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Check if any alien has reached the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _update_screen(self):
        # color the background
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
