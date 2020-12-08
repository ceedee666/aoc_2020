from pathlib import Path
from collections import defaultdict
import typer


app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return lines

def parse_input(lines):
    return list(map(
        lambda l: defaultdict(int, {"operation": l[:3], "value": int(l[4:])}),
        lines))


def run_instructions(instructions):
    accumulator = 0
    instruction_pointer = 0

    current_instruction = instructions[instruction_pointer]

    while current_instruction["execution_count"] == 0:
        current_instruction["execution_count"] += 1
        
        operation = current_instruction["operation"]
        
        if operation == "nop":
            instruction_pointer += 1
        elif operation == "jmp":
            instruction_pointer += current_instruction["value"]
        elif operation == "acc":
            accumulator += current_instruction["value"]
            instruction_pointer += 1
        
        current_instruction = instructions[instruction_pointer]
    return accumulator


@app.command()
def part1(input_file: str):
    accumulator = run_instructions(parse_input(read_input_file(input_file)))
    print(f"The value of the accumulator is {accumulator}")


if __name__ == "__main__":
    app()