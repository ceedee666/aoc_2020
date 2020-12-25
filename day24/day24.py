from pathlib import Path
from functools import reduce
import re
import typer


app = typer.Typer()

MOVEMENT = {"e" : (1, 0),
            "se": (0, 1),
            "sw": (-1, 1),
            "w" : (-1, 0),
            "nw": (0, -1),
            "ne": (+1, -1)}


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return lines


def conv_steps_to_moves(line):
    re_iter = re.finditer("[ns]?[ew]", line)
    return list(map(lambda m: MOVEMENT[m[0]], re_iter))


def flip_tile_by_moves(black_tiles, moves):
    tile = reduce(lambda t, m: (t[0] + m[0], t[1] + m[1]), moves, (0, 0))

    if tile in black_tiles:
        black_tiles -= set([tile])
    else:
        black_tiles |= set([tile])

    return black_tiles


@app.command()
def part1(input_file_path: str):
    all_moves = list(map(lambda l: conv_steps_to_moves(l),
                         read_input_file(input_file_path)))
    black_tiles = reduce(lambda s, m: flip_tile_by_moves(s, m), all_moves, set())
    print(f"{len(black_tiles)} tiles are left with the black side up.")


if __name__ == "__main__":
    app()
