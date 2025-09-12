import sys
import pygame

class KomptonInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Kompton Invasion")

    def run_game(game):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, and run the game
    ki = KomptonInvasion()
    ki.run_game()