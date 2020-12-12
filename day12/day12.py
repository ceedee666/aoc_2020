from pathlib import Path
from functools import reduce
import typer

DIRECTIONS = ["E", "S", "W", "N"]

app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda l: (l[0], int(l[1:])), lines))


def move(pos, step):
    operation, dist = step

    if operation in "WE":
        if operation == "W":
            dist *= -1
        new_pos = (pos[0], pos[1] + dist)

    if operation in "NS":
        if operation == "S":
            dist *= -1
        new_pos = (pos[0] + dist, pos[1])

    return new_pos


def turn(direction, step):
    operation, dist = step

    if operation in "RL":
        if operation == "L":
            dist *= -1
        dir_index = DIRECTIONS.index(direction)
        new_dir_index = (dir_index + dist // 90) % len(DIRECTIONS)
        return DIRECTIONS[new_dir_index]


def move_ship(ship, step):
    new_ship = dict()

    if step[0] == "F":
        step = (ship["dir"], step[1])

    if step[0] in DIRECTIONS:
        new_ship["pos"] = move(ship["pos"], step)
        new_ship["dir"] = ship["dir"]
    else:
        new_ship["pos"] = ship["pos"]
        new_ship["dir"] = turn(ship["dir"], step)

    return new_ship


@app.command()
def part1(input_file: str):
    ship = {"pos": (0, 0), "dir": "E"}
    r = reduce(lambda s, p: move_ship(s, p), read_input_file(input_file), ship)
    distance = abs(r["pos"][0]) + abs(r["pos"][1])
    print(f"The manhatten distance of the ships position is {distance}.")


if __name__ == "__main__":
    app()
