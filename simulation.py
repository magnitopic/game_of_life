DIFF = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_alive_neighbors(grid, cell: tuple[int, int], ROWS, COLS):
    count = 0
    for d in DIFF:
        neighbor = (cell[0] + d[0], cell[1] + d[1])
        if ((neighbor[0] < 0 or neighbor[1] < 0) or (neighbor[0] >= COLS or neighbor[1] >= ROWS)):
            continue
        if neighbor in grid:
            count += 1
    return count


def get_checkable_positions(grid, ROWS, COLS) -> list[tuple[int, int]]:
    """ We need a list of all the cells that might be counted as alive in the 
      next iteration. So we take into account all currently alive cells and their
      neighbors. """
    checkable_neighbors = []
    for cell in grid:
        for d in DIFF:
            neighbor = (cell[0] + d[0], cell[1] + d[1])
            if ((neighbor[0] < 0 or neighbor[1] < 0) or (neighbor[0] >= COLS or neighbor[1] >= ROWS)):
                continue
            if neighbor not in checkable_neighbors:
                checkable_neighbors.append(neighbor)
    return checkable_neighbors


def check_positions(grid, ROWS, COLS):
    new_grid = []
    cells_to_check = get_checkable_positions(grid, ROWS, COLS)
    for i in cells_to_check:
        n_neighbors = count_alive_neighbors(grid, i, ROWS, COLS)
        if n_neighbors == 3:
            new_grid.append(i)
        elif (i in grid) and (n_neighbors == 2):
            new_grid.append(i)
    return new_grid


def simulation(grid: set, ROWS, COLS):
    """ Main game logic """
    new_grid = check_positions(grid, ROWS, COLS)
    return new_grid
