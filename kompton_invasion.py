import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PAYER_SPEED = 5

# Alien Settings
ALIEN_WIDTH = 50
ALIEN_HEIGHT = 50
ALIEN_SPEED = 3

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kompton Invasion")

#  Load images
player_img = pygame.image.load('spaceship.png')
alien_img = pygame.image.load('alien.png')

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2

    def update(self, direction):
        if direction == "UP":
            self.rect.y -= PLAYER_SPEED
        elif direction == "DOWN":
            self.rect.y += PLAYER_SPEED
        elif direction == "LEFT":
            self.rect.x -= PLAYER_SPEED
        elif direction == "RIGHT":
            self.rect.x += PLAYER_SPEED

        # Keep player within screen boundaries
        self.rect.x = max(0, min(SCREEN_WIDTH - PLAYER_WIDTH, self.rect.x))
        self.rect.y = max(0, min(SCREEN_HEIGHT - PLAYER_HEIGHT, self.rect))

    # Define the alien class
    class Alien(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.transform.scale(alien_img, (ALIEN_WIDTH, ALIEN_HEIGHT))
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH, + 200)
            self.rect.y = random.randrange(SCREEN_HEIGHT - ALIEN_HEIGHT)
            self.speed = random.randint(1, ALIEN_SPEED)

        def update(self):
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH + 200)
                self.rect.y = random.randrange(SCREEN_HEIGHT - ALIEN_HEIGHT)
                self.speed = random.randint(1, ALIEN_SPEED)
                

