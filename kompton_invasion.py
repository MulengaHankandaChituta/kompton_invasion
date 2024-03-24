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
PLAYER_SPEED = 5  # Corrected typo in variable name

# Alien Settings
ALIEN_WIDTH = 50
ALIEN_HEIGHT = 50
ALIEN_SPEED = 1

# Projectile settings
PROJECTILE_WIDTH = 5
PROJECTILE_HEIGHT = 10
PROJECTILE_SPEED = 8

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kompton Invasion")

# Load images
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
        self.projectiles = pygame.sprite.Group() # Group to store projectiles

    def update(self, direction=None):
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
        self.rect.y = max(0, min(SCREEN_HEIGHT - PLAYER_HEIGHT, self.rect.y))

    def shoot(self):
        # Create a new projectile
        projectile = Projectile(self.rect.centerx, self.rect.top)
        self.projectiles.add(projectile,)

# Define the alien class
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(alien_img, (ALIEN_WIDTH, ALIEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = 0  # Set y-coordinate to 0 to ensure aliens appear at the top
        self.speed = random.randint(1, ALIEN_SPEED)

    def update(self, direction):
         self.rect.y += self.speed
         if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randrange(SCREEN_WIDTH)
            self.rect.y = 0
            self.speed = random.randint(1, ALIEN_SPEED)
# define the projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PROJECTILE_WIDTH, PROJECTILE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        # Move the projectile up
        self.rect.y -= PROJECTILE_SPEED
        # Remove the projectile if it goes of the screen
        if self.rect.bottom < 0:
            self.kill()

# Create sprite groups
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()

# Create player object
player = Player()
all_sprites.add(player)

# Main game loop
running = True
score = 0
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()  # Shoot when SPACE key is pressed
    # Get keyboard input
    keys = pygame.key.get_pressed()
    direction = None
    if keys[pygame.K_UP]:
        direction = "UP"
    elif keys[pygame.K_DOWN]:
        direction = "DOWN"
    elif keys[pygame.K_LEFT]:
        direction = "LEFT"
    elif keys[pygame.K_RIGHT]:
        direction = "RIGHT"

    # Spawn aliens
    if len(aliens) < 5:
        alien = Alien()
        all_sprites.add(alien)
        aliens.add(alien)

    # Update sprites
    all_sprites.update(direction)

    # Update projectiles
    player.projectiles.update()

    # Check for collisions
    collisions = pygame.sprite.groupcollide(player.projectiles, aliens, True, True)
    for projectile, collided_aliens in collisions.items():
        collisions = pygame.sprite.spritecollide(projectile, aliens, True)
        for alien in collided_aliens:
            score += 1

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    player.projectiles.draw(screen)

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, RED)
    screen.blit(text, (10, 10))
    
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()