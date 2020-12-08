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
    infinite_loop = False

    while instruction_pointer < len(instructions) \
            and not infinite_loop:
      
        instructions[instruction_pointer]["execution_count"] += 1
        
        if instructions[instruction_pointer]["execution_count"] <= 1:

            operation = instructions[instruction_pointer]["operation"]
        
            if operation == "nop":
                instruction_pointer += 1
            elif operation == "jmp":
                instruction_pointer += instructions[instruction_pointer]["value"]
            elif operation == "acc":
                accumulator += instructions[instruction_pointer]["value"]
                instruction_pointer += 1
        
        else:
            infinite_loop = True
            
    return accumulator, infinite_loop


@app.command()
def part1(input_file: str):
    accumulator, _ = run_instructions(parse_input(read_input_file(input_file)))
    print(f"The value of the accumulator is {accumulator}")


if __name__ == "__main__":
    app()
