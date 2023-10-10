import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for screen size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Static TV")

# Function to generate random static noise
def generate_static(screen):
    for _ in range(10000):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        screen.set_at((x, y), color)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate static noise
    generate_static(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
