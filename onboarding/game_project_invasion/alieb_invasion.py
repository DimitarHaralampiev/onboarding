import sys
import pygame

from game_project_invasion.settings import Settings
from game_project_invasion.ship import Ship
import game_function as gf


def run_game():
    # Initialize game and create screen object#
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship
    ship = Ship(screen)

    # Start mani loop for game
    while True:
        # Watch for keyboard and mouse
        gf.check_events()

        # Redraw the screen during each pass through the loop.
        gf.event_screen(ai_settings, screen, ship)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
