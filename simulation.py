DIFF = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def check_neighbors(grid, square: tuple[int, int], ROWS, COLS):
    count = 0
    for d in DIFF:
        neighbor = (square[0] + d[0], square[1] + d[1])
        if ((neighbor[0] < 0 or neighbor[1] < 0) or (neighbor[0] > ROWS or neighbor[1] > COLS)):
            continue
        if neighbor in grid:
            count += 1
    return count


def get_checkable_positions(grid, ROWS, COLS) -> list[tuple[int, int]]:
    checkable_neighbors = []
    for square in grid:
        for d in DIFF:
            neighbor = (square[0] + d[0], square[1] + d[1])
            if ((neighbor[0] < 0 or neighbor[1] < 0) or (neighbor[0] > ROWS or neighbor[1] > COLS)):
                continue
            if neighbor not in checkable_neighbors:
                checkable_neighbors.append(neighbor)
    return checkable_neighbors


def check_positions(grid, ROWS, COLS):
    new_grid = []
    cells_to_check = get_checkable_positions(grid, ROWS, COLS)
    for i in cells_to_check:
        n_neighbors = check_neighbors(grid, i, ROWS, COLS)
        if n_neighbors == 3:
            new_grid.append(i)
        elif (i in grid) and (n_neighbors == 2):
            new_grid.append(i)
    return new_grid


""" Main game logic """
def simulation(grid: set, ROWS, COLS):
    new_grid = check_positions(grid, ROWS, COLS)
    return new_grid
