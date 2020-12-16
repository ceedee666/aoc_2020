from pathlib import Path
from functools import reduce

import typer

app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return list(map(lambda l: l.strip(), lines))


def parse_rules(lines):
    rules = dict()

    for line in lines:
        field, ranges = line.split(": ")
        range1, range2 = ranges.split(" or ")
        low1, high1 = map(lambda v: int(v), range1.split("-"))
        low2, high2 = map(lambda v: int(v), range2.split("-"))
        allowed_values = set(range(low1, high1 + 1)).union(range(low2, high2 + 1))

        rules[field] = allowed_values

    return rules


def parse_input(lines):
    i = lines.index("")
    rules = parse_rules(lines[0:i])
    ticket = list(map(lambda v: int(v), lines[i+2].split(",")))
    other_tickets = list(map(
                             lambda l: list(map(lambda v: int(v), l.split(","))),
                             lines[i+5:]))

    return rules, ticket, other_tickets


def check_value(v, rules):
    return any(map(lambda r: v in r, rules.values()))


def invalid_values(ticket, rules):
    checked_values = map(lambda v: (v, check_value(v, rules)), ticket)
    invalid_values = filter(lambda v: v[1] == False, checked_values)
    return list(map(lambda v: v[0], invalid_values))


def check_tickets(tickets, rules):
    return list(map(lambda t: (t, invalid_values(t, rules)), tickets))


@app.command()
def part1(input_file: str):
    rules, ticket, other = parse_input(read_input_file(input_file))
    checked_tickets = check_tickets(other, rules)
    error_rate = sum(reduce(lambda l, t: l + t[1], checked_tickets, []))

    print(f"The error rate of the tickets is {error_rate}")

if __name__ == "__main__":
    app()
