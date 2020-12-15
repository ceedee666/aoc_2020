from pathlib import Path
from collections import defaultdict

import typer

INPUT = "2,20,0,4,1,17"

app = typer.Typer()


def play_turn(game):
    turn = game["turn"]
    number = game["number"]

    prev_turn = game["memory"][number]

    if prev_turn == 0:
        new_number = 0
    else:
        new_number = turn - prev_turn

    game["memory"][number] = turn

    game["number"] = new_number
    game["turn"] = turn + 1

    return game


def init_game(init_string):
    init_data = init_string.split(",")

    game = {}
    game["memory"] = defaultdict(int)

    for t, n in enumerate(init_data[:-1]):
        game["memory"][int(n)] = t + 1

    game["turn"] = len(init_data)
    game["number"] = int(init_data[-1])

    return game


def play_2020_turns(game):
    while game["turn"] < 2020:
        game = play_turn(game)
    return game


@app.command()
def part1():
    game = init_game(INPUT)
    result = play_2020_turns(game)

    number = result["number"]
    print(f"The 2020th number is {number}.")


@app.command()
def part2():
    print()


if __name__ == "__main__":
    app()
