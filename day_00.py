import os
from time import perf_counter as pfc
from tools.AOC_input import get_input

DAY: int = int(os.path.basename(__file__)[4:6])


def solve(data: list, part1=False, part2=False):
    print(data[:10])
    return part1, part2


def main(example):

    if example:
        with open("example.txt") as f:
            data = f.read().split("\n")
    else:
        data: list = get_input(DAY)

    start = pfc()
    print(*solve(data))
    print(f"{((pfc() - start) * 1000):5.1f} ms")


if __name__ == '__main__':
    main(True)
    # main(False)
