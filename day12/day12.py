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


def move_ship(ship, step):
    move, dist = step
    new_ship = dict()

    if move == "F":
        move = ship["dir"]

    if move in "WE":
        if move == "W":
            dist *= -1
        new_ship["pos"] = (ship["pos"][0], ship["pos"][1] + dist)
        new_ship["dir"] = ship["dir"]

    if move in "NS":
        if move == "S":
            dist *= -1
        new_ship["pos"] = (ship["pos"][0] + dist, ship["pos"][1])
        new_ship["dir"] = ship["dir"]

    if move in "RL":
        if move == "L":
            dist *= -1
        dir_index = DIRECTIONS.index(ship["dir"])
        new_dir_index = (dir_index + dist // 90) % len(DIRECTIONS)
        new_ship["pos"] = ship["pos"]
        new_ship["dir"] = DIRECTIONS[new_dir_index]

    return new_ship


@app.command()
def part1(input_file: str):
    ship = {"pos": (0, 0), "dir": "E"}
    r = reduce(lambda s, p: move_ship(s, p), read_input_file(input_file), ship)
    distance = abs(r["pos"][0]) + abs(r["pos"][1])
    print(f"The manhatten distance of the ships position is {distance}.")


if __name__ == "__main__":
    app()
