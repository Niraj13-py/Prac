import pygame
import time

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 400))
screen.fill((255, 255, 255))

# Ball position and direction
x, y = 0, 200
x_dir, y_dir = 1, 1

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw red ball
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25, 0)
    pygame.display.flip()
    
    # Wait a bit
    time.sleep(0.05)

    # Erase ball (draw white over it)
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 25, 0)
    pygame.display.flip()

    # Move ball
    x += x_dir * 10
    y += y_dir * 10

    # Bounce off walls
    if y >= 400 or y <= 0:
        y_dir = -y_dir
    if x >= 800 or x <= 0:
        x_dir = -x_dir
clock.tick(60)
# Exit
pygame.quit()
