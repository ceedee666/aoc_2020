from pathlib import Path
from functools import reduce
import typer


app = typer.Typer()


def read_input_file(input_file_path):
    p = Path(input_file_path)

    with p.open() as f:
        lines = f.readlines()

    return lines


def parse_ingredience(lines):
    ingredience_lists = []

    for line in lines:
        elements = line.split()
        idx = elements.index("(contains")
        ingr = elements[:idx]
        allg = list(map(lambda s: s.strip(",)"), elements[idx+1:]))

        ingredience_lists.append({"ing": ingr, "all": allg})

    return ingredience_lists


def ingredience_without_allergenes(ingredience_lists):
    allg_ing_map = {}

    for ingr_list in ingredience_lists:
        ingr_set = set(ingr_list["ing"])

        for allg in ingr_list["all"]:
            if allg in allg_ing_map:
                allg_ing_map[allg] = allg_ing_map[allg] & ingr_set
            else:
                allg_ing_map[allg] = ingr_set

    all_ing = {ing for il in ingredience_lists for ing in il["ing"]}
    ingr_wo_allg = all_ing - {ing for allg in allg_ing_map for ing in allg_ing_map[allg]}

    return ingr_wo_allg


@app.command()
def part1(input_file: str):
    ingredience_lists = parse_ingredience(read_input_file(input_file))
    ingr_wo_allg = ingredience_without_allergenes(ingredience_lists)
    s = len(list(filter(lambda i: i in ingr_wo_allg,
            [ing for il in ingredience_lists for ing in il["ing"]])))

    print(f"Ingredient that cannot be allergenes appear {s} times.")


if __name__ == "__main__":
    app()
