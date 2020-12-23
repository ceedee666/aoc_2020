import typer


app = typer.Typer()


INPUT = list(map(int, "974618352"))


def pickup(idx, cups):
    if idx + 1 == len(cups):
        pick = cups[:3]
    elif idx + 4 < len(cups):
        pick = cups[idx+1:idx+4]
    else:
        pick = cups[idx+1:]
        rest = 3 - len(pick)
        pick += cups[:rest]
    return pick


def shift_cups(idx, cup, cups):
    new_idx = cups.index(cup)
    shift = new_idx - idx
    if shift != 0:
        new_cups = cups[shift:]+cups[:shift]
    else:
        new_cups = cups
    return new_cups


def play_crab_cups_round(idx, cups):
    min_cup_value = min(cups)
    max_cup_value = max(cups)

    current_cup = cups[idx]
    destination = current_cup - 1 if current_cup > min_cup_value else max_cup_value
    pick = pickup(idx, cups)

    while destination in pick:
        destination = destination - 1 if destination > min_cup_value else max_cup_value
    new_cups = [c for c in cups if c not in pick]

    dest_idx = new_cups.index(destination)
    new_cups = new_cups[:dest_idx+1] + pick + new_cups[dest_idx+1:]
    new_cups = shift_cups(idx, current_cup, new_cups)

    return new_cups


def play_crab_cups(cups, pad, rounds=100):
    if len(cups) < pad:
        cups = cups + list(range(max(cups)+1, pad +1))

    for i in range(rounds):
        cups = play_crab_cups_round(i % len(cups), cups)
    return cups


@app.command()
def part1():
    cups = play_crab_cups(INPUT)
    idx = cups.index(1)
    result = "".join(list(map(str, cups[idx+1:] + cups[:idx])))
    print(f"The labels after cup 1 are: {result}")


@app.command()
def part2():
    cups = INPUT + list(range(max(INPUT), 1_000_001))
    cups = play_crab_cups(cups, 10_000_000)
    idx = cups.index(1)

    print(f"The result for part 2 is: {cups[idx+1] * cups[idx+2]}")


if __name__ == "__main__":
    app()
