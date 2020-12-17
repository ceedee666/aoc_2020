from pathlib import Path
from functools import reduce
import typer


ACTIVE = "#"
INACTIVE = "."


app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda l: l.strip(), lines))


def parse_grid(lines):
    grid = init_empty_grid(len(lines), len(lines[0]), 1)

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == ACTIVE:
                grid[i][j][0] = ACTIVE

    return grid


def init_empty_grid(size_x, size_y, size_z):
    return [[[
        INACTIVE for _ in range(size_z)]
        for _ in range(size_y)]
        for _ in range(size_x)]


def neighbour_coordinates(coordinate):
    x, y, z = coordinate

    coordinates = [(a, b, c)
                   for a in range(x-1, x+2)
                   for b in range(y-1, y+2)
                   for c in range(z-1, z+2)]

    coordinates.remove(coordinate)

    return coordinates


def active_neighbours(coordinate, grid):
    coordinates = neighbour_coordinates(coordinate)
    active = reduce(lambda s, c: s + 1 if cell_state(c, grid) == ACTIVE else s, coordinates, 0)
    return active


def all_coordinates(grid):
    coordinates = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            for z in range(len(grid[x][y])):
                coordinates.append((x, y, z))
    return coordinates


def active_cell_coordinates(grid):
    return list(filter(lambda c: grid[c[0]][c[1]][c[2]] == ACTIVE, all_coordinates(grid)))


def cell_state(coordinate, grid):
    x, y, z = coordinate

    if x < 0 or y < 0 or z < 0:
        return INACTIVE
    if x >= len(grid) or y >= len(grid[0]) or z >= len(grid[0][0]):
        return INACTIVE

    return grid[x][y][z]


def print_grid(grid):
    for z in range(len(grid[0][0])):
        print("-----------------------------------")
        print(f"Z = {z}")

        for x in range(len(grid)):
            line = ""
            for y in range(len(grid[0])):
                line += grid[x][y][z]
            print(line)


def execute_step(grid):
    '''
    Calculates the new state of the grid based on the following rules:
    - If a cell is active and exactly 2 or 3 of its neighbors are also active,
      the cube remains active. Otherwise, the cell becomes inactive.
    - If a cell is inactive but exactly 3 of its neighbors are active,
      the cell becomes active.
    '''

    new_grid = init_empty_grid(
        len(grid) + 2, len(grid[0]) + 2, len(grid[0][0]) + 2)

    for c in all_coordinates(new_grid):
        x, y, z = c

        old_coordinate = (x-1, y-1, z-1)
        state = cell_state(old_coordinate, grid)
        active_neighbours_count = active_neighbours(old_coordinate, grid)

        if state == ACTIVE and active_neighbours_count in [2, 3]:
            new_grid[x][y][z] = ACTIVE
        elif state == INACTIVE and active_neighbours_count == 3:
            new_grid[x][y][z] = ACTIVE

    return new_grid


@app.command()
def part1(input_file: str):
    grid = parse_grid(read_input_file(input_file))
    for _ in range(6):
        grid = execute_step(grid)
    print(f"After six cycles {len(active_cell_coordinates(grid))} cubes are active.")


if __name__ == "__main__":
    app()
