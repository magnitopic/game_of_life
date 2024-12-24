""" from game_of_life import HEIGHT, WIDTH, CELL_SIZE """


""" def check_neighbors(grid, square):
    count = 0
    for i in range(-1, 1):
        for j in range(-1, 1):
            if ((i < 0 or i > WIDTH/CELL_SIZE) or
                    (j < 0 or i > HEIGHT/CELL_SIZE)):
                continue
            print(next(item for item in grid if item["x"]
                       == i+square["x"] and item["x"] == j + square["y"]))

    return


def check_positions(grid):
    for i in grid:
        check_neighbors(grid, i) """


""" Main game logic """


def simulation(grid):
    """ check_positions(grid) """
    pass
