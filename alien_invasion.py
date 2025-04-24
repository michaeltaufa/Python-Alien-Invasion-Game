"""
Program Name: Alien Invasion
Description:
    This program will be focused on building an Alien Invasion video game
    using Pygame.
Name: Michael Taufa
Date: 2025-04-24
"""

import sys

import pygame 

# NOTE: First, create a Class that will be the attribute of the video game,
    # Alien Invasion. This class will be focused on building basic attributes
    # for running a game such as opening a window and closing a window.


class AlienInvasion:

    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        """Start the main loop for the game."""
        while True:

            # NOTE: Watch for keyboard and mouse events.
            # NOTE: This is known as an "Event Loop", that will respond
            # based on user input

            for event in pygame.event.get():
            vent.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drtawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Create a game instance and run game
    ai = AlienInvasion()
    ai.run_game()
