import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (173, 216, 230)  # Light blue background
CIRCLE_RADIUS = 10
MAX_CIRCLES = 10

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hiir")

# Circle list
circles = []

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if len(circles) >= MAX_CIRCLES:
                circles.pop(0)  # Remove the oldest circle
            circles.append({'pos': pos, 'radius': CIRCLE_RADIUS, 'color': random_color()})
        
    # Clear the screen
    screen.fill(BG_COLOR)
    
    # Draw circles
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['pos'], circle['radius'])

    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.delay(30)

pygame.quit()
