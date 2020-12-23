import typer


app = typer.Typer()


INPUT = list(map(int, "974618352"))


def init_linked_list(cups, pad):
    ll = ["NOT USED"] + [i+1 for i in range(1, pad+1)]

    for i in range(len(cups)-1):
        ll[cups[i]] = cups[i+1]

    if len(cups) == pad:
        ll[cups[-1]] = cups[0]
    else:
        ll[cups[-1]] = len(cups)+1
        ll[-1] = 1
    head = cups[0]
    return head, ll


def play_crab_cups_round(head, ll):
    dest = head-1 if head > 1 else len(ll)-1

    nc1 = ll[head]
    nc2 = ll[nc1]
    nc3 = ll[nc2]

    while dest in [nc1, nc2, nc3]:
        dest = dest-1 if dest > 1 else len(ll)-1

    ll[head] = ll[nc3]

    dest_nc = ll[dest]
    ll[dest] = nc1
    ll[nc3] = dest_nc

    return ll[head], ll


def cups_list(head, ll):
    result = []
    current = head

    while len(result) < len(ll)-1:
        result.append(current)
        current = ll[current]

    return result


def play_crab_cups(cups, pad, rounds):
    """
    Use list as a linked list. The index is the label of the cups,
    the value is the next cup.
    """
    head, ll = init_linked_list(cups, pad)
    for _ in range(rounds):
        head, ll = play_crab_cups_round(head, ll)

    print(len(ll))
    return head, ll


@app.command()
def part1():
    head, ll = play_crab_cups(INPUT, len(INPUT), 100)
    c = cups_list(head, ll)
    idx = c.index(1)
    result = "".join(list(map(str, c[idx+1:] + c[:idx])))
    print(f"The labels after cup 1 are: {result}")


@app.command()
def part2():
    head, ll = play_crab_cups(INPUT, 1_000_000, 10_000_000)
    c = cups_list(head, ll)
    idx = c.index(2)

    print(f"The result for part 2 is: {c[idx+1] * c[idx+2]}")


if __name__ == "__main__":
    app()
