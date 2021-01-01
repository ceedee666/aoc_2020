import typer


PK1 = 15733400
PK2 = 6408062


app = typer.Typer()


def transform_step(value=1, subject_nr=7):
    value *= subject_nr
    value %= 20201227
    return value


def transform(subject_nr, loop_size):
    value = 1
    for _ in range(loop_size):
        value = transform_step(value, subject_nr)
    return value


def determine_loop_size(public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        loop_size += 1
        value = transform_step(value)
    return loop_size


@app.command()
def part1():
    loop_size_1 = determine_loop_size(PK1)
    loop_size_2 = determine_loop_size(PK2)

    print("The encryption key is: ")
    print(f"- Calculated using private key one: {transform(PK1, loop_size_2)}")
    print(f"- Calculated using private key two: {transform(PK2, loop_size_1)}")


if __name__ == "__main__":
    app()
