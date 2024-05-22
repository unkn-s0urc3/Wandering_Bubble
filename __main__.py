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

# List to store previous positions
trail = []

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

    # Add current position to trail list
    trail.append((x, y))
    # Keep only the last 50 positions in the trail list
    trail = trail[-50:]

    # Clear the screen with a white color to gradually fade out the previous trail
    screen.fill(WHITE)

    # Draw the trail
    for pos in trail:
        # Calculate alpha value based on position in the trail
        alpha = 255 - int(200 * trail.index(pos) / len(trail))
        # Draw semi-transparent circle at each position in the trail
        pygame.draw.circle(screen, (0, 128, 255, alpha), pos, radius)

    # Draw the bubble with gradient fill at the current position
    pygame.draw.circle(screen, (0, 128, 255), (x, y), radius)  # Outer color
    pygame.draw.circle(screen, (135, 206, 250), (x, y), int(radius * 0.9))  # Middle color
    pygame.draw.circle(screen, (173, 216, 230), (x, y), int(radius * 0.6))  # Inner color

    # Update the display
    pygame.display.flip()

    # Control movement speed
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()