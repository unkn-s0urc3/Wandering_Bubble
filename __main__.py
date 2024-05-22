import pygame
import sys

# Initialize Pygame
pygame.init()

# Set window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wandering Bubble")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Bubble parameters
radius = 50
x, y = width // 2, height // 2
speed_x, speed_y = 5, 5

# Main program loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bubble movement
    x += speed_x
    y += speed_y

    # Check collision with window boundaries
    if x - radius < 0 or x + radius > width:
        speed_x = -speed_x
    if y - radius < 0 or y + radius > height:
        speed_y = -speed_y

    # Clear the screen
    screen.fill(WHITE)

    # Draw the bubble
    pygame.draw.circle(screen, BLUE, (x, y), radius)

    # Update the display
    pygame.display.flip()

    # Control movement speed
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
