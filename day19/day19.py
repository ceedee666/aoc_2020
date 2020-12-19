from pathlib import Path
from functools import reduce
from itertools import chain, product

import re
import typer


app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    lines = list(map(lambda s: s.strip(), lines))
    i = lines.index("")
    return lines[:i], lines[i+1:]


def parse_rules(rule_strings):
    rules = {r.split(": ")[0]:
             r.split(": ")[1].strip('"').split()
             for r in rule_strings}
    return rules


def build_regex(rule_index, rules):
    if rules[rule_index][0] in "ab":
        return rules[rule_index][0]

    regex = "("
    for value in rules[rule_index]:
        if value == "|":
            regex += value
        else:
            regex += build_regex(value, rules)

    return regex + ")"


@app.command()
def part1(input_file: str):
    rule_strings, messages = read_input_file(input_file)
    regex = build_regex("0", parse_rules(rule_strings))

    matching_msg_count = len(list(filter(
                         lambda m: re.fullmatch(regex, m), messages)))
    print(f"{matching_msg_count} messages match the rules.")


if __name__ == "__main__":
    app()
