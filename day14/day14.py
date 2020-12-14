from pathlib import Path
from functools import reduce
from operator import add

import typer

app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    program = []

    for line in lines:
        op, val = line.strip().split(" = ")
        if op == "mask":
            program.append({"op": "mask", "val": val})
        else:
            program.append({"op": "mem",
                            "add": int(op[4:-1]),
                            "val": int(val)})
    return program


def apply_bin_mask(mask, val):
    bin_val = f"{bin(val)[2:]:0>36}"
    bin_result = ""

    for i, c in enumerate(mask):
        if c in "01":
            bin_result += c
        else:
            bin_result += bin_val[i]

    return int(bin_result, 2)


def execute_instruction(memory, instruction):
    if instruction["op"] == "mask":
        memory["mask"] = instruction["val"]
    elif instruction["op"] == "mem":
        val = apply_bin_mask(memory["mask"], instruction["val"])
        memory[instruction["add"]] = val

    return memory


def execute_initialization(program):
    memory = reduce(lambda m, e: execute_instruction(m, e), program, dict())
    memory.pop("mask")
    return sum(memory.values())


@app.command()
def part1(input_file: str):
    program = read_input_file(input_file)
    result = execute_initialization(program)
    print(f"The sum of all values in memory is {result}.")


if __name__ == "__main__":
    app()
