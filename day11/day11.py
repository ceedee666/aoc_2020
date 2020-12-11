from pathlib import Path
from functools import reduce
from itertools import chain
from collections import Counter

import typer

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda l: list(l.strip()), lines))


def neighbor_indicies(pos, x_size, y_size):
    indices = [(x, y) for x in range(pos[0]-1, pos[0]+2)
                      for y in range(pos[1]-1, pos[1]+2)]
    indices.remove(pos)
    return list(filter(lambda p: p[0] >= 0 and p[1] >= 0
                              and p[0] < x_size and p[1] < y_size, indices))


def occupied_neighbors(pos, grid):
    neighbors = neighbor_indicies(pos, len(grid), len(grid[0]))
    return reduce(
            lambda a, n: a + 1 if grid[n[0]][n[1]] == OCCUPIED else a,
            neighbors, 0)


def next_state(pos, grid):
    state = grid[pos[0]][pos[1]]

    if state == FLOOR:
        return FLOOR
    elif state == EMPTY and occupied_neighbors(pos, grid) == 0:
        return OCCUPIED
    elif state == OCCUPIED and occupied_neighbors(pos, grid) >= 4:
        return EMPTY
    else:
        return state


def simulate_step(grid):
    next_grid = []
    for x in range(len(grid)):
        next_row = []
        for y in range(len(grid[0])):
            next_row.append(next_state((x, y), grid))
        next_grid.append(next_row)
    return next_grid


def simulator(start_grid):
    current = start_grid
    while True:
        current = simulate_step(current)
        yield current


@app.command()
def part1(input_file: str):
    previous_grid = []
    current_grid = read_input_file(input_file)
    sim = simulator(current_grid)

    while current_grid != previous_grid:
        previous_grid = current_grid
        current_grid = next(sim)

    counter = Counter(chain.from_iterable(current_grid))

    print(f"The number of occupied seats is {counter[OCCUPIED]}")


if __name__ == "__main__":
    app()
