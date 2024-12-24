import pygame
import random
from simulation import simulation


pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 5
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

""" 
[
        {x: 5,
    y: 1},
    {x:7,
    y: 3}
]
 """

grid = []

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")


def draw_screen():
    """Draw the current game state"""
    screen.fill(BLACK)
    for i in grid:
        pygame.draw.rect(screen, WHITE, (i["x"], i["y"], CELL_SIZE, CELL_SIZE))
    pygame.display.flip()


def random_initial_positions():
    n_squares = random.randrange(20, 300)
    for _ in range(n_squares):
        x_axis = random.randrange(0, WIDTH, CELL_SIZE)
        y_axis = random.randrange(0, HEIGHT, CELL_SIZE)
        grid.append({"x": x_axis, "y": y_axis})


def main():
    running = True
    paused = False
    clock = pygame.time.Clock()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0] // CELL_SIZE
                row = mouse_pos[1] // CELL_SIZE
                # Update your grid based on click

        # Game logic
        if not paused:
            simulation()

        # Drawing
        draw_screen()
        random_initial_positions()

        # Control game speed
        clock.tick(10)  # 10 FPS

    pygame.quit()


if __name__ == "__main__":
    random_initial_positions()
    main()
