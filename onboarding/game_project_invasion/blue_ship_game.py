import sys
import pygame

from game_project_invasion import game_function as gf

from game_project_invasion.settings import Settings
from game_project_invasion.ship import Ship


class BlueShip:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
        ))
        pygame.display.set_caption('Blue Ship Game')

        self.ship = Ship(self, self.screen)

    def run_game(self):
        while True:
            gf.check_events(self.ship)
            self.ship.update()

            # Make a ship
            ship = Ship(self.ship.ai_settings, self.ship.screen)

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()
            self.clock.tick(60)


game = BlueShip()
game.run_game()
