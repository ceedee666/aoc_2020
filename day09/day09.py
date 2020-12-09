from pathlib import Path

import itertools
import typer


app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda l: int(l), lines))


def is_number_valid(preamble, number):
    preamble_sums = map(sum, itertools.combinations(set(preamble), 2))
    return number in preamble_sums


def check_validity(numbers, length):
    return map(
            lambda e: (is_number_valid(numbers[e[0] - length:e[0]], e[1]), e[1]),
            enumerate(numbers[length:], length))


@app.command()
def part1(input_file: str, pl: int = 25):
    checked_numbers = check_validity(read_input_file(input_file), pl)
    invalid_numbers = list(filter(lambda n: not n[0], checked_numbers))

    print(f"The value of the first invalid number is {invalid_numbers[0][1]}.")


if __name__ == "__main__":
    app()
