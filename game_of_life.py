import pygame
import random
from simulation import simulation

pygame.init()
random.seed(42)
# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
COLS, ROWS = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

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
        pygame.draw.rect(
            screen, WHITE, (i[0] * CELL_SIZE, i[1] * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE-1))
    pygame.display.flip()


def random_initial_positions():
    board = [(x, y) for x in range(COLS) for y in range(ROWS)]
    random.shuffle(board)
    global grid
    grid = board[:500]


def main():
    global grid
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
                cell = (col, row)
                if cell in grid:
                    grid.pop(grid.index(cell))
                else:
                    grid.append(cell)

        # Game logic
        if not paused:
            grid = simulation(grid, ROWS, COLS)

        # Drawing
        draw_screen()

        # FPS
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    random_initial_positions()
    main()
