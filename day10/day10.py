from pathlib import Path
from collections import Counter
from functools import reduce
import typer


app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda l: int(l), lines))


def count_jolt_differences(adapters):
    adapters.append(0)
    sorted_adapters = sorted(adapters)
    sorted_adapters.append(max(sorted_adapters)+3)

    differences = map(
            lambda e: e[1] - sorted_adapters[e[0] - 1],
            enumerate(sorted_adapters[1:], 1))
    
    return Counter(differences)


@app.command()
def part1(input_file: str):
    jolt_differences = count_jolt_differences(read_input_file(input_file))
    print(f"The solution for part 1 is {jolt_differences[1] * jolt_differences[3]}.")


@app.command()
def part2(input_file: str):
    jolt_differences = count_jolt_differences(read_input_file(input_file))
    print(f"The solution for part 1 is {jolt_differences[1] * jolt_differences[3]}.")


if __name__ == "__main__":
    app()
