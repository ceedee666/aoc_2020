import day11

def prepare_data():
    s0 = ["L.LL.LL.LL",
          "LLLLLLL.LL",
          "L.L.L..L..",
          "LLLL.LL.LL",
          "L.LL.LL.LL",
          "L.LLLLL.LL",
          "..L.L.....",
          "LLLLLLLLLL",
          "L.LLLLLL.L",
          "L.LLLLL.LL"]

    
    s1 = ["#.##.##.##",
          "#######.##",
          "#.#.#..#..",
          "####.##.##",
          "#.##.##.##",
          "#.#####.##",
          "..#.#.....",
          "##########",
          "#.######.#",
          "#.#####.##"]
    
    s2 = ["#.LL.L#.##",
          "#LLLLLL.L#",
          "L.L.L..L..",
          "#LLL.LL.L#",
          "#.LL.LL.LL",
          "#.LLLL#.##",
          "..L.L.....",
          "#LLLLLLLL#",
          "#.LLLLLL.L",
          "#.#LLLL.##"]

    result = []

    result.append(list(map(lambda l: list(l), s0)))
    result.append(list(map(lambda l: list(l), s1)))
    result.append(list(map(lambda l: list(l), s2)))

    return result


def test_simulate_step():
    test_data = prepare_data()
    assert test_data[1] == day11.simulate_step(test_data[0])
    assert test_data[2] == day11.simulate_step(test_data[1])


def test_simulate():
    test_data = prepare_data()
    simulator = day11.simulator(test_data[0])
    assert test_data[1] == next(simulator)
    assert test_data[2] == next(simulator)




    
