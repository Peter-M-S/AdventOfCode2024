import os
from time import perf_counter as pfc
from aocd import get_data


def solve(data, part1=False, part2=False):
    print(data)
    return part1, part2


def main(example):
    file_name = "example.txt" if example else os.path.basename(__file__)[:-3] + ".txt"
    if not os.path.exists(file_name):
        with open(file_name, "w"):
            print(f"{file_name} created")
    with open(file_name) as f:
        data = f.read().split("\n")

    print(get_data(session="53616c7465645f5fd430b4ef350fbc4cd2443bd44e238ef4efaf075baf0a1d22debb10c63677f20cda1a72c7acbf2f0bbbd6876ed5b1fc0a39a6b00c07a5ff07", day=1, year=2024))

    start = pfc()
    print(*solve(data))
    print(f"{((pfc() - start) * 1000):5.1f} ms")


if __name__ == '__main__':
    main(True)
    # main(False)
