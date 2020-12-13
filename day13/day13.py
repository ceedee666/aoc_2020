from pathlib import Path
from functools import reduce
import typer


app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return int(lines[0]), lines[1].strip().split(",")


@app.command()
def part1(input_file: str):
    time, busses = read_input_file(input_file)
    busses = map(lambda i: int(i), filter(lambda s: s.isdigit(), busses))
    wating_time = reduce(lambda a, b: a if a[1] < b[1] else b,
                           map(lambda b: (b, b - time % b), busses))
    print(f"The bus ID is {wating_time[0]} and the waiting time {wating_time[1]}.")
    print(f"Therefor the solution to the puzzle is {wating_time[0] * wating_time[1]}.")


if __name__ == "__main__":
    app()
